from urllib import request, error
import re, time, threading, queue

urlqueue = queue.Queue()
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
opener = request.build_opener()
opener.addheaders = [headers]
request.install_opener(opener)
listurl = []


# 代理
def use_proxy(proxy_addr, url):
    # try:
    #     from urllib import request
    #     proxy = request.ProxyHandler({'http':proxy_addr})
    #     opener = request.build_opener(proxy, request.HTTPHandler)
    #     request.install_opener(opener)
    #     data = request.urlopen(url).read().decode('utf-8')
    #     return data
    # except error.URLError as e:
    #     if hasattr(e, 'code'):
    #         print(e.code)
    #     if hasattr(e, 'reason'):
    #         print(e.reason)
    #     time.sleep(10)
    # except Exception as e:
    #     print('exception:' + str(e))
    #     time.sleep(1)
    try:
        data = request.urlopen(url).read().decode('utf-8')
        return data
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(1)
    except Exception as e:
        print('exception:' + str(e))
        time.sleep(1)


# 获取文章链接
class geturl(threading.Thread):
    def __init__(self, url, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.proxy = proxy
    def run(self):
        if not isinstance(self.url, str):
            raise RuntimeError('参数必须为URL字符串')
        try:
            html = use_proxy(self.proxy, self.url)
            html = str(html)
            urlpth = '<div class="txt-box">[\s\S]*?href="(.*?)"'
            listurl.append(re.compile(urlpth).findall(html))
            for i in range(0, len(listurl)):
                time.sleep(1)
                for j in range(0, len(listurl[i])):
                    url = listurl[i][j]
                    url = url.replace('amp;', '')
                    urlqueue.put(url)
                    urlqueue.task_done()
        except error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)
            time.sleep(1)
        except Exception as e:
            print('exception:' + str(e))
            time.sleep(1)



# 获取文章标题
class gettitle(threading.Thread):
    def __init__(self, proxy):
        threading.Thread.__init__(self)
        self.proxy = proxy
    def run(self):
        while(True):
            try:
                url = urlqueue.get()
                html = use_proxy(self.proxy, url)
                html = str(html)
                titlepat = 'var msg_title = "(.*?)"'
                title = re.compile(titlepat).findall(html)
                if title.__len__() != 0:
                    for t in title:
                        print(t)
                else:
                    print('未获取到标题')
            except error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)


# 并行控制线程
class control(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            print('程序执行中...')
            time.sleep(10)
            if urlqueue.empty():
                print('程序执行完毕')
                exit()

proxy1 = '119.6.136.122:80'
proxy2 = '121.231.155.12:6666'
print('欢迎查询微信公众号文章...')
keyword = input('请输入查询的关键词:')
page = input('请输入查询的页数：')
page = int(page)

t2 = gettitle(proxy1)
t2.start()
t3 = control()
t3.start()
for i in range(1, page + 1):
    url = 'http://weixin.sogou.com/weixin?query=' + request.quote(keyword) + '&type=2&page=' + str(i)
    t1 = geturl(url, proxy1)
    t1.start()

