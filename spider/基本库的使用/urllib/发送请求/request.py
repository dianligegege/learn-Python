from urllib import request, parse

import ssl
# 通过导入ssl模块把证书验证改成不用验证
ssl._create_default_https_context = ssl._create_unverified_context

# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# decode 进行编码，不然全是\n
# print(response.read().decode('utf-8'))

# class urllib.request.Request(ur1, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# 或使用add_header()来添加headers
# req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
