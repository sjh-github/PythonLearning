# 爬取百度首页
# 导入模块
from urllib import request

# 伪装成浏览器
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener=request.build_opener()
opener.addheaders=[headers]
request.install_opener(opener)

# 设置超时
file = request.urlopen("http://www.baidu.com", timeout=1)
# 读取全部数据
data = file.read()
# 读取第一行数据
dataline = file.readline()
# 写入文件
fhandle = open("D:/baidu.html", "wb")
fhandle.write(data)
fhandle.close()

print(dataline)
print(data)


