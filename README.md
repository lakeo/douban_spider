# 豆瓣小组用户资料下载工具
- 使用scrapy框架编写
- 自动切换agent
- 自动登录
- 自动下载用户头像及用户名

## 使用方法
安装scrapy:
```
pip install scrapy
```

修改settings.py:
```
# 图片的存放地址
IMAGES_STORE = '/store/path/'
```

修改.base_spider.py:
```
    start_urls = (
        # 设置需要爬的小组url,例如：
        'https://www.douban.com/group/movie_view/members',
    )
```


运行:
```
$ scrapy crawl user_spider
```
