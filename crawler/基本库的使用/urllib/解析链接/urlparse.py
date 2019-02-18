from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
# scheme://netloc/path ;params?query#fragment

# api用法 urllib.parse.urlparse(urlstring, scheme=”, allow_fragments=True)

result1 = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result1)

# 链接自带协议的不能更改
result2 = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result2)


# allow_fragments  是否忽略frafments

result3 = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result3) # fragment为空，comment被解析为query,若无query，则继续向上解析为path


# 调用方式为属性名调用和索引调用
print(result[0], result.scheme)