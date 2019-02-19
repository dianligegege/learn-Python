import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

# 添加参数
data1 = {
    'name': 
}