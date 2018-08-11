# -*- coding: utf-8 -*-
# import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ScrapyCrawlDemo.items import ScrapycrawldemoItem


class CrawldemoSpider(CrawlSpider):
    name = 'CrawlDemo'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('http://.*?sohu.com.*?'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ScrapycrawldemoItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        try:
            i["name"] = response.xpath("//div[@class='list16']/ul/li/a/@title").extract()
            i["link"] = response.xpath("//div[@class='list16']/ul/li/a/@href").extract()
        except Exception as e:
            print(e)
        return i
