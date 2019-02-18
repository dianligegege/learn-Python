import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)
print(response)

# 保存cookie  txt格式
cookie1 = http.cookiejar.MozillaCookieJar('cookies.txt')
# 缺少中间几部生成的cookies文件没有内容
cookie1.save(ignore_discard=True, ignore_expires=True)

# 保存cookie为LWP格式
cookie2 = http.cookiejar.LWPCookieJar('cookie2.txt')
handler = urllib.request.HTTPCookieProcessor(cookie2)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie2.save(ignore_discard=True, ignore_expires=True)

# 调用cookie
cookie3 = http.cookiejar.LWPCookieJar()
cookie3.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie3)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))