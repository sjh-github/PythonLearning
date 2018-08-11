# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import codecs
# import json
import pymysql


class DangdangbookPipeline(object):
    def __init__(self):
        # print("打开文件")
        # self.file = codecs.open("D:\\DangDangBestSellBook.json", "wb", encoding="utf-8")
        # 打开数据库
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="dangdangbestsellbook")

    def process_item(self, item, spider):
        print("写入数据库")
        print("数目：" + str(len(item["title"])))
        for j in range(0, len(item["title"])):
            print("开始写入" + str(j + 1))
            title = item["title"][j]
            author = item["author"][j]
            commentNum = item["commentNum"][j]
            url = item["url"][j]
            # price = item["price"][j]
            # price2 = item["price2"][j]
            # data = {"书名": title, "作者": author, "评论数": commentNum, "链接": url, "实体书价格": price, "电子书价格": 0}
            # dataline = json.dumps(dict(data), ensure_ascii=False)
            # dataline2 = dataline + "\n"
            # self.file.write(dataline2)
            try:
                sql = "insert into BestSellBook(title, author, commentNum, url) values('" + title + "','" + author + "','" + commentNum + "','" + url + "')"
                self.conn.query(sql)
            except Exception as e:
                print(e)
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.conn.commit()
        print("关闭数据库")
        self.conn.close()
