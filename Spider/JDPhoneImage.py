# 爬取京东手机图片

import re
from urllib import request

def craw(url, page):
    html1 = request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = 'D:\\JingDong\\' + str(page) + str(x) + '.jpg'
        imageurl = 'http://' + imageurl
        print(imageurl)
        try:
            request.urlretrieve(imageurl, filename=imagename)
        except request.HTTPError as e:
            print(e.code)
            print(e.reason)
        x += 1

# 爬取1，2两页
for i in range(1, 3):
    url = 'http://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
    craw(url, i)