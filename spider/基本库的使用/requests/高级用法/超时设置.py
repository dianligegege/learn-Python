import requests

# 超过0.1秒没响应就报错
# r = requests.get("https://www.taobao.com", timeout=0.1)
# print(r.status_code)

# 分别指定链接和读取的响应时间
r1 = requests.get('https://taobao.com', timeout=(5, 30))
print(r1.status_code)

# 不设置timeout或设置为none代表无限等待