# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs


class ScrapytestPipeline(object):
    def __init__(self):
        print("初始化")
        self.file = codecs.open("D:\\mydata.txt", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        print("输出到文件： " + str(item))
        self.file.write(str(item))
        return item

    def close_spider(self, spider):
        print("关闭")
        self.file.close()
