# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class ScrapyxmldemoPipeline(object):
    def __init__(self):
        print("初始化")
        self.file = codecs.open("D:\\mydata.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False)
        print("输出到文件： " + data)
        self.file.write(data)
        return item

    def close_spider(self, spider):
        print("结束")
        self.file.close()
