from urllib import request
import re

def getcontent(url, page):
    header = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
    opener = request.build_opener()
    opener.addheaders = [header]
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    # 用户的正则表达式
    userpat = '<h2>\s*(.+?)\s*</h2>'
    # 段子内容的正则表达式
    contentpat = '<div class="content">.*\s*<span>\s*(.*)'
    # 寻找出所有用户
    userlist = re.compile(userpat).findall(data)
    # 寻找出所有的内容
    contentlist = re.compile(contentpat).findall(data)
    x = 1
    # 通过for循环遍历段子内容并将内容分别赋给相应的变量
    print('contentlist: ' + str(contentlist.__len__()))
    for content in contentlist:
        content = content.replace('<br/>', '\n')
        name = 'content' + str(x)
        exec(name + '=content')
        x += 1
    y = 1
    for user in userlist:
        name = 'content' + str(y)
        print('用户' + str(page) + str(y) + '是：' + user)
        print('内容是：')
        exec('print(' + name + ')')
        print('\n')
        y += 1


for i in range(1, 2):
    url = 'https://www.qiushibaike.com/8hr/page/' + str(i)
    getcontent(url, i)