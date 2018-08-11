# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapycrawldemoPipeline(object):
    def process_item(self, item, spider):
        try:
            for i in range(0, len(item["name"])):
                print(item["name"][i])
                print(item["link"][i])
                print("----------------")
        except Exception as e:
            print(e)
        return item
