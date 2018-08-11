# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 评论数
    commentNum = scrapy.Field()
    # 书籍链接
    url = scrapy.Field()
    # 实体书价格
    price = scrapy.Field()
    # 电子书价格
    price2 = scrapy.Field()
