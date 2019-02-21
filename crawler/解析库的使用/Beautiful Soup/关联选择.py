from bs4 import BeautifulSoup

html = '''
<html>
    <body>
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

## 1.子节点和子孙节点

#子节点 使用contents
print(soup.p.contents) # 返回一个p所有子节点的列表
# 使用children获取子节点
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 使用descendants获取所有子孙节点
for i, child in enumerate(soup.p.descendants):
    print(i, child)


## 2.父节点和祖先节点

# 获取父节点 使用partent
print(soup.a.parent)
# 获取祖先节点
print(soup.parents) # 生成器类型
print(list(enumerate(soup.a.parents)))


## 3.兄弟节点

# 紧邻
print('next sibling', soup.a.next_sibling) 
print('pre sibling', soup.a.previous_sibling)

# 所有 是生成器类型
print('next siblings', list(enumerate(soup.a.next_siblings))) 
print('pre siblings', list(enumerate(soup.a.previous_siblings)))


