# urllib Get Demo 模仿百度搜索
from urllib import request

# 伪装成浏览器
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener = request.build_opener()
opener.addheaders = [headers]
request.install_opener(opener)

url = "https://www.baidu.com/s?wd="
# 搜索关键字
key = "中国"
# 对中文进行编码
key_code = request.quote(key)
# 完整的请求链接
url_all = url + key_code
# 保存结果
response = request.urlretrieve(url_all, filename="D:\\中国.html")
