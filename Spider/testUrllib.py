# urllib尝试
# import urllib.request
# # 连接URL
# file = urllib.request.urlopen('http://www.baidu.com')
# data = file.read()
# # 打开文件
# fhandle = open('D:/baidu.html', 'wb')
# fhandle.write(data)
# fhandle.close()
#
# # 读取网页并保存到文件中
# filename = urllib.request.urlretrieve('http://www.baidu.com', filename='D:/test.html')


# 添加消息头模拟浏览器
# import urllib.request
# url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
# print(urllib.request.urlopen(url, timeout=10).read())
# req = urllib.request.Request(url)
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
# print(urllib.request.urlopen(req, timeout=10).read())


# GET请求百度搜索信息
# from urllib import request
# key = '石佳豪'
# key_code = request.quote(key)
# url = 'http://www.baidu.com/s?wd=' + key_code
# req = request.Request(url)
# data = request.urlopen(req).read()
# fhandle = open('E:/keyword.html', 'wb')
# fhandle.write(data)
# fhandle.close()


# POST登陆请求
# from urllib import request, parse
# url = 'http://www.iqianyue.com/mypost/'
# postdata = parse.urlencode({
#     'name': '石佳豪',
#     'pass': 'Aa123'
# }).encode('utf-8')
# req = request.Request(url, postdata)
# data = request.urlopen(req).read()
# fhandle = open('E:/5.html', 'wb')
# fhandle.write(data)
# fhandle.close()


# 使用代理
# def use_proxy(proxy_addr, url):
#     from urllib import request
#     proxy = request.ProxyHandler({'http': proxy_addr})
#     opener = request.build_opener(proxy, request.HTTPHandler)
#     request.install_opener(opener)
#     data = request.urlopen(url).read().decode('utf-8')
#     return data
#
#
# proxy_addr = '110.73.41.221:8123'
# data = use_proxy(proxy_addr, "http://www.baidu.com")
# print(len(data))


# DebugLogger
# from urllib import request
# httphd = request.HTTPHandler(debuglevel=1)
# httpshd = request.HTTPHandler(debuglevel=1)
# opener = request.build_opener(httphd, httpshd)
# request.install_opener(opener)
# data = request.urlopen('http://edu.51cto.com')


# URLError
# from urllib import request,error
# try:
#     request.urlopen('http://blog.csdn.net')
#     print('OK!')
# except error.HTTPError as e:
#     print(e.code)
#     print(e.reason)
# except error.URLError as e:
#     print(e.reason)