# -*- coding: utf-8 -*-
import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest, HtmlResponse

from douban_pic.items import UserItem


class UserCrawlSpider(CrawlSpider):
    name = "user_spider"
    download_delay = 0.1

    allowed_domains = []

    start_urls = (
        'https://www.douban.com/group/movie_view/members',
    )

    rules = (
            Rule(LinkExtractor(allow=(r'https://www.douban.com/group/movie_view/members?start=\d+'))),
            Rule(LinkExtractor(allow=(r'https://www.douban.com/people/.*/')), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)

        if not sel.xpath('//div[@class="nav-logo"]'):
            yield Request(url=response.url, dont_filter=True)

        img = sel.xpath('//div[@class="basic-info"]/img[@src]/@src').extract_first()
        username = sel.xpath('//div[@class="info"]/h1/text()[1]').extract_first()

        if img and username:
            item = UserItem()
            item['image'] = img
            item['username'] = username.strip()
            yield item

    def start_requests(self):
        return [Request("https://accounts.douban.com/login",
                    meta={'cookiejar': 1}, callback=self.post_login)]

    # 为了模拟浏览器，我们定义httpheader
    post_headers = {
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    }

    # FormRequeset
    def post_login(self, response):
        logging.info('开始登录')
        return [FormRequest.from_response(response,
                                      url='https://accounts.douban.com/login',
                                      meta={'cookiejar': response.meta['cookiejar']},
                                      headers=self.post_headers,  # 注意此处的headers
                                      formdata={
                                          'redir': 'https://www.douban.com/',
                                          'form_email': '258789822@qq.com',
                                          'form_password': '*****',
                                      },
                                      callback=self.after_login,
                                      dont_filter=True
                                      )]

    def after_login(self, response):
        logging.info('登录成功')
        for url in self.start_urls:
            yield Request(url, meta={'cookiejar': response.meta['cookiejar']})

    def _requests_to_follow(self, response):
        """重写加入cookiejar的更新"""
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = Request(url=link.url, callback=self._response_downloaded)
                # 下面这句是我重写的
                r.meta.update(rule=n, link_text=link.text, cookiejar=response.meta['cookiejar'])
                yield rule.process_request(r)