import requests

# 1.设置cookie
requests.get('http://httpbin.org/cookies/set/number/123456789')
# 2.获取cookie
r = requests.get('http://httpbin.org/cookies')
# 3.获取不到
print(r.text)

#使用Session试试
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r1 = s.get('http://httpbin.org/cookies')
# 获取成功
print(r1.text)
