from bs4 import BeautifulSoup

# 使用lxml解析器
soup1 = BeautifulSoup('<p>hello</p>', 'lxml')
print(soup1.p.string)

# 基本用法
html = '''
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p name="p2">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
            <a href="http://example.com/tillie" class="sister" id="link3">Tilie</a>;
            and they lived at the bottom of a well.
        </p>
        <p class="story">
            ...
        </p>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(soup.title.string)

## 节点选择器（适用于单个节点解构层次清晰）

# 选择元素
print(soup.head) 
print(soup.p) # 打印第一个p元素

# 提取信息
print(soup.title.name) # 获取节点名称
print(soup.p.attrs) # 获取属性
print(soup.p.attrs['name'])
print(soup.p['name']) # 获取属性简易方法 name属性唯一所以返回单个字符串
print(soup.p['class']) # class可能有多个值，所以返回列表

# 获取内容
print(soup.p.string) # 获取的是第一个p

## 嵌套选择
print(soup.head.title.string)

## 关联选择
# 看单文件