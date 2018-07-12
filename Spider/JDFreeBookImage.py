import re
from urllib import request


def craw(url, maxcount):
    count = 0
    html = request.urlopen(url).read()
    html = str(html)
    with open('D:/1.html', 'w') as f:
        f.write(html)
    imageptn = '<img .+? src="(//.+?\.jpg)">'
    imageurllist = re.compile(imageptn).findall(html)
    print(imageurllist.__len__())
    for imageurl in imageurllist:
        if count > maxcount:
            break
        imageurl = 'http:' + imageurl
        print(imageurl)
        imagename = 'D:/Baidu/' + str(count) + '.jpg'
        request.urlretrieve(imageurl, imagename)
        count += 1


url = 'http://list.jd.com/list.html?cat=5272,5276'
craw(url, 100)