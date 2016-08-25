# -*- coding: utf-8 -*-

# Scrapy settings for douban_pic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_pic'

SPIDER_MODULES = ['douban_pic.spiders']
NEWSPIDER_MODULE = 'douban_pic.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# 设置每次抓取的时间间隔,单位s
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
        #'douban_pic.randomproxy.RandomProxy': 100,
        'douban_pic.middlewares.rotate_useragent.RotateUserAgentMiddleware': 543,

        # 'yourspider.randomproxy.RandomProxy': 100,
        # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

ITEM_PIPELINES = {
        # 'scrapy.pipelines.images.ImagesPipeline':1
        'douban_pic.pipelines.DoubanPicPipeline':1
}
IMAGES_STORE = '/Users/xiaolu/Documents/source/douban_user_download/images/' # your path for store img

# Retry many times since proxies often fail
RETRY_TIMES = 3
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# PROXY_LIST = '/path/to/proxy/list.txt'
