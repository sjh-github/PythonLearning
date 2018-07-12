import re
from urllib import request

def getlink(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
    opener = request.build_opener()
    opener.addheaders = [headers]
    request.install_opener(opener)
    file = request.urlopen(url)
    data = str(file.read())
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link


url = 'http://blog.csdn.net/'
linklist = getlink(url)
for link in linklist:
    print(link[0])