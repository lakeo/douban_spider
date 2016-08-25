# -*- coding: utf-8 -*-

import scrapy


class UserItem(scrapy.Item):
    image = scrapy.Field()
    username = scrapy.Field()