# 使用代理IP爬取百度首页
from urllib import error
# 定义使用代理函数
def use_proxy(proxy_addr, url):
    from urllib import request
    proxy = request.ProxyHandler({"http":proxy_addr})
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    return request.urlopen(url).read()

proxy_addr = "101.236.22.141:8866"
try:
    data = use_proxy(proxy_addr, "http://www.shijiahao.com")
    fhandle = open("D:\\baidu.html", "wb")
    fhandle.write(data)
    fhandle.close()
except error.HTTPError as e:
    print(e.code)
    print(e.reason)
