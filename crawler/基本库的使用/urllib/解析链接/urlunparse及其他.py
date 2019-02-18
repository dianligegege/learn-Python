from urllib.parse import urlunparse, urlsplit, urlunsplit, urljoin, urlencode, parse_qs, parse_qsl, quote, unquote

url = 'http://www.baidu.com/index.html;user?id=5#comment'

#urlunparse  反向urlparse,参数必须为六个
data = ['http', 'www.baidu.com', 'index.html', '', 'a=6&b=5', 'comment']
print(urlunparse(data))


# urlsplit 不解析params,返回五个参数的元数组
print(urlsplit(url))

# urlunsplit 五个参数
data1 = ['http', 'www.baidu.com', 'index.html', 'a=6&b=5', 'comment']
print(urlunsplit(data1))

# urljoin base_url只提供scheme,netloc,path三个参数，第二个参数可以覆盖base_url
print(urljoin('http://baidu.com', 'index.html'))
print(urljoin('http://baidu.com?wd=abc', 'https://www.baidu.index.html'))

# urlencode()
query = {
    'name': 'zhangli',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(query)
print(url)

# parse_qs
query1 = 'name=zhangli&age=34'
print(parse_qs(query1)) # 生成字典{'name': ['zhangli'], 'age': ['34']}
print(parse_qs(query1)['name'][0]) # zhangli

#parse_qsl
print(parse_qsl(query1)) # 生成[('name', 'zhangli'), ('age', '34')]

# quote 将内容编码为url编码的格式
keyword = '鼻子哈哈'
url = 'http://www.baidu.com?wd=' + quote(keyword)
print(url)

# unquote 用来解码
print(unquote(url))
