# 使用Cookie Demo

# 导入模块
from urllib import request, parse, error
from http import cookiejar

url1 = "http://115.159.71.92/hongruan/web/login"
postdata = parse.urlencode({
    "email":"",
    "password":""
}).encode("utf-8")
req = request.Request(url1, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
# 创建CookieJar
cjar = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cjar))
request.install_opener(opener)
try:
    data = request.urlopen(req).read()
    fhandle = open("D:\\upackage1.html", "wb")
    fhandle.write(data)
    fhandle.close()
except error.HTTPError as e:
    print("url1: " + str(e.code))
    print("url1: " + str(e.reason))


url2 = "http://115.159.71.92/hongruan/web/indexPage/provideTaskPersonal"
try:
    request.urlretrieve(url2, filename="D:\\upackage2.html")
except error.HTTPError as e:
    print("url2: " + str(e.code))
    print("url2: " + str(e.reason))