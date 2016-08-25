# -*- coding: utf-8 -*-

import re

from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class DoubanPicPipeline(ImagesPipeline):
    
    headers = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'referer': '',
    }

    def get_media_requests(self, item, info):
        return [Request(item.image, headers=self.get_headers(item.image), meta={'username': item['username']})]

    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

    def get_images(self, response, request, info):
        print("get images")
        for key, image, buf, in super(DoubanPicPipeline, self).get_images(response, request, info):
            if self.CONVERTED_ORIGINAL.match(key):
                key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return key.replace('full', response.meta['username'])

    def get_headers(self, url):
        headers = self.headers
        ref = re.sub(r'img\d\.doubanio\.com/view/photo/raw/public/p(.*)\.jpg', \
                r'movie.douban.com/photos/photo/\g<1>/', url)
        headers['referer'] = ref
        return headers

