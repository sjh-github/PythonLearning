# urllib Post Demo
# 测试链接：http://www.iqianyue.com/mypost/

# 导入模块
from urllib import request, parse

url = "http://www.iqianyue.com/mypost/"
# 数据编码
postdata = parse.urlencode({
    "name":"我的昵称",
    "pass":"w123456"
}).encode("utf-8")

req = request.Request(url, postdata)
# 模拟浏览器
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
req.add_header = [headers]

data = request.urlopen(req).read()
fhandle = open("D:\\postDemo.html", "wb")
fhandle.write(data)
fhandle.close()

