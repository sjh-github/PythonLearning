# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ScrapyXmlDemo.items import ScrapyxmldemoItem


class MyxmlspiderSpider(XMLFeedSpider):
    name = 'MyXmlSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes'  # you can change this; see the docs
    itertag = 'rss'  # change it accordingly,开始迭代的第一个节点

    def parse_node(self, response, selector):
        i = ScrapyxmldemoItem()
        i["title"] = selector.xpath("/rss/channel/item/title/text()").extract()
        i["link"] = selector.xpath("/rss/channel/item/link/text()").extract()
        i["author"] = selector.xpath("/rss/channel/item/author/text()").extract()
        for j in range(len(i["title"])):
            print("第" + str(j + 1) + "篇文章")
            print("标题： " + i["title"][j])
            print("链接： " + i["link"][j])
            print("作者： " + i["author"][j])
            print("****************************")
        return i
