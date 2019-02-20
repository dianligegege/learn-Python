import logging
import requests
from requests.packages import urllib3

# 实际可以正常访问，12306应该已添加证书，假设不能访问
response = requests.get('https://www.12306.cn')
print(response.status_code)

# 下面这样写会出现警告，建议我们指定证书
r1 = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 设置忽略警告
urllib3.disable_warnings()
r2 = requests.get('https://www.12306.cn', verify=False)
print(r2.status_code)

# 或者捕获警告到日志
logging.captureWarnings(True)
r3 = requests.get('https://www.12306.cn', verify=False)
print(r3.status_code)

# 或者使用本地证书
# r4 = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)