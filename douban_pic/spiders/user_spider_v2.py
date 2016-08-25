# -*- coding: utf-8 -*-
import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest, HtmlResponse

from douban_pic.items import UserItem


class UserCrawlSpider(CrawlSpider):
    name = "user_spider_v2"
    download_delay = 0.1

    allowed_domains = []

    start_urls = (
        'https://www.douban.com/group/movie_view/members',
        'https://www.douban.com/group/26926/members',
        'https://www.douban.com/group/Dear-momo/',
        'https://www.douban.com/group/explore',
    )

    rules = (
            Rule(LinkExtractor(allow=(r'https://www.douban.com/group/.*/members\?start=\d')), follow=True),
            Rule(LinkExtractor(allow=(r'https://www.douban.com/group/(?!topic).*/')), follow=True),
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