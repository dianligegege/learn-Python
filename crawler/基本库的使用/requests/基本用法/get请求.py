import re
import requests

r = requests.get('http://httpbin.org/get')
# print(r.text)

# 添加参数
data1 = {
    'name': 'zhangli',
    'age': 23
}
r = requests.get('http://httpbin.org/get', params=data1)
print(r.text)
print(type(r.text)) # class 'str'
print(r)
print(type(r)) # class 'requests.models.Response'
print(r.json())
print(type(r.json())) # class 'dict'

# 抓取网页 添加headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("http://www.zhihu.com/expore", headers=headers)
pattern = re.compile('expore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取二进制数据
# r1 = requests.get("https://jd.com/favcion.ico")
# print(type(r1.text))
# print(r.text)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)