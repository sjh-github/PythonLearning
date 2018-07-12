# 伪装成浏览器模板（代理可省略）
from urllib import request
from http import cookiejar
url = 'http://news.163.com/16/0825/09/BVA8A9U500014SEH.html'
# headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
#            'Connection':'keep-alive',
#            'Referer':'http://www.163.com/'}
headers = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'), ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'), ('Connection', 'keep-alive'), ('Referer', 'http://www.163.com/')]
# 设置cookie
cjar = cookiejar.CookieJar()
proxy = request.ProxyHandler({'http':'127.0.0.1:8888'})
opener = request.build_opener(proxy, request.HTTPHandler, request.HTTPCookieProcessor(cjar))
# 建立空列表，为了以指定格式存储头信息
# headall = []
# 通过for循环遍历循环字典，构造出指定格式的headers信息
# for key, value in headers.items():
#     item = (key, value)
#     headall.append(item)
# 将指定格式的headers信息添加好
opener.addheaders = headers
request.install_opener(opener)
data = request.urlopen(url).read()
fhandle = open('D:/3.html', 'wb')
fhandle.write(data)
fhandle.close()
