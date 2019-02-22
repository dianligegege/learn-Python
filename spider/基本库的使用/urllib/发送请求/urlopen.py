'''urllib.request'''
import urllib.request


import ssl
# 通过导入ssl模块把证书验证改成不用验证
ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# data参数
import urllib.parse
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
res1 = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(res1.read())

# timeout 参数

# 超时报错
# res2 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

# 使用 try except
import socket
import urllib.error

try:
    res3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 其他参数context,cafile,capath