# -*- coding: utf-8 -*-
import scrapy
from ScrapyTest.items import ScrapytestItem


class ScrapytestSpider(scrapy.Spider):
    name = 'ScrapyTest'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
                  'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml']

    def __init__(self, myurl=None, *args, **kwargs):
        super(ScrapytestSpider, self).__init__(*args, **kwargs)
        if myurl is not None:
            myurllist = myurl.split(",")
            self.start_urls = myurllist
        print("要爬取的网址为： %s" % self.start_urls)

    def parse(self, response):
        item = ScrapytestItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
