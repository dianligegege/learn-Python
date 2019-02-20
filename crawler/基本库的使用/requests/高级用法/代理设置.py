import requests

# 使用代理，要用自己的代理服务器
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080"
}

requests.get("https://www.taobao.com", proxies=proxies)

# 若代理使用HTTP Basic Auth
proxies1 = {
    "http": "http://user:password@10.10.1.10:3128/",
}
requests.get("http://www.taobao.com", proxies=proxies1)

# 还支持SOCKS协议的代理
proxies2 = {
    "http": "sock5://user:password@host:port",
    "https": "sock5://user:password@host:port"
}
requests.get("http://taobao.com", proxies=proxies2)