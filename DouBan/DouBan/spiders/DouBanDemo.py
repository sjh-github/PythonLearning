# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from scrapy.http import Request, FormRequest


class DoubandemoSpider(scrapy.Spider):
    name = 'DouBanDemo'
    allowed_domains = ['douban.com']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def start_requests(self):
        print("start_requests")
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        print("parse")
        captha = response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captha) > 0:
            print("需要验证码")
            localpath = "D:\\captcha.png"
            request.urlretrieve(captha[0], filename=localpath)
            print("请到D盘根目录查看验证码")
            captcha_value = input("请输入验证码：")
            data = {
                "form_email": "252355189@qq.com",
                "form_password": "252355189",
                "captcha-solution": captcha_value,
                "redir": "https://www.douban.com/people/152166985/"
            }
        else:
            print("不需要验证码")
            data = {
                "form_email": "252355189@qq.com",
                "form_password": "252355189",
                "redir": "https://www.douban.com/people/152166985/"
            }
        print("登陆中")
        return [FormRequest.from_response(response, meta = {"cookiejar": response.meta["cookiejar"]},
                headers = self.headers,
                formdata = data,
                callback = self.next)]

    def next(self, response):
        print("登陆成功")
        xtitle = "/html/head/title/text()"
        xnotetitle = "//div[@class = 'note-header p12']/a/@title"
        xnotetime = "//div[@class = 'note-header p12']//span[@class = 'p1']/text()"
        xnotecontent = "//div[@class = 'mbtr2']/div[@class = 'note']/text()"
        xnoteurl = "//div[@class = 'note-header p12']/a/@href"
        # 提取信息
        title = response.xpath(xtitle).extract()
        notetitle = response.xpath(xnotetitle).extract()
        notetime = response.xpath(xnotetime).extract()
        notecontent = response.xpath(xnotecontent).extract()
        noteurl = response.xpath(xnoteurl).extract()
        print("网页标题是：" + title[0])
        for i in range(0, len(notetitle)):
            print("第" + (i + 1) + "篇文章的信息如下：")
            print("标题：" + notetitle[i])
            print("时间：" + notetime[i])
            print("内容：" + notecontent[i])
            print("URL： " + noteurl[i])
            print("------------------------------------------------")