# Cookie
from urllib import request, parse
from http import cookiejar
url = 'http://cas.hdu.edu.cn/cas/login'
postdata = parse.urlencode({
    'username': '15196120',
    'password': 'hdu15196120',
}).encode('utf-8')
req = request.Request(url, postdata)
req.add_header('UserAgent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')

# # 创建CookieJar对象
# cjar = cookiejar.CookieJar()
# # 创建cookie处理器
# opener = request.build_opener(request.HTTPCookieProcessor(cjar))
# # 安装为全局对象
# request.install_opener(opener)
#
# file = opener.open(req)
# data = file.read()
# file = open('D:/hdu.html', 'wb')
# file.write(data)
# file.close()

data = request.urlopen(req).read()
fhandle = open('D:/hdu.html', 'wb')
fhandle.write(data)
fhandle.close()

url2 = 'http://i.hdu.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage'
req2 = request.Request(url2, postdata)
req2.add_header('UserAgent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
data2 = request.urlopen(url2).read()
fhandle = open('D:/hdu2.html', 'wb')
fhandle.write(data2)
fhandle.close()
