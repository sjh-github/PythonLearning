# -*- coding: utf-8 -*-
import scrapy
from DangDangBook.items import DangdangbookItem
from scrapy.http import Request


class DangdangbestsellbookSpider(scrapy.Spider):
    name = 'DangDangBestSellBook'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1']

    def parse(self, response):
        item = DangdangbookItem()
        item["title"] = response.xpath("//div[@class='name']/a/text()").extract()
        item["author"] = response.xpath("//div[@class='publisher_info']/a[1]/@title").extract()
        item["commentNum"] = response.xpath("//div[@class='star']/a/text()").extract()
        item["url"] = response.xpath("//div[@class='star']/a/@href").extract()
        item["price"] = response.xpath("//div[@class='price']/p[1]/span[@class='price_n']/text()").extract()
        item["price2"] = response.xpath("//div[@class='price']/p[last()]/span/text()").extract()
        yield item
        for i in range(2, 100):
            url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-" + str(i)
            yield Request(url, callback=self.parse)
