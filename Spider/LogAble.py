# 开启DebugLogger
from urllib import request
httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPHandler(debuglevel=1)
opener = request.build_opener(httphd, httpshd)
request.install_opener(opener)
data = request.urlopen('http://edu.51cto.com')