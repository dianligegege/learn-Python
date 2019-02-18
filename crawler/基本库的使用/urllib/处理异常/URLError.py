from urllib import request, error
import socket

# try:
#     response = request.urlopen('http://cuqingcai.com/index.html')
# except error.URLError as e:
#     print(e.reason)

# 先使用子类错误捕获，再用父类错误捕获
try:
    response = request.urlopen('http://cuqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError as e:
    print(e)
    print(e.reason)

# 错误还可能不是字符串，而是对象
try:
    response1 = request.urlopen('http://www.baidu.com', timeout=0.0001)
except error.URLError as e:
    print(e)
    print(e.reason)
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')