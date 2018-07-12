# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem


class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = ('http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
                  'http://slide.mil.news.sina.com.cn//slide_8_193_45192.html#p=1',
                  'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml')

    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print(item['urlname'])

    def __init__(self, myurl=None, *args, **kwargs):
        super(WeisuenSpider, self).__init__(*args, **kwargs)
        print("要爬取的网址为：%s" % myurl)
        self.start_urls = ("%s" % myurl)
