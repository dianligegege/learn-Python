from bs4 import BeautifulSoup
import re

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

## find_all()
## name
print(soup.find_all(name='ul'))
# 结果是一个列表，每个元素都是bs4.element.Tag类型，可以进行嵌套查询
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li')) 

# attrs
print(soup.find_all(attrs={'id': 'list-2'}))
# 或者简写
print(soup.find_all(id='list-2'))
# 因为class是python关键字，所以加一个下划线，而且class有多个也可以匹配（不用想Xpath使用contains）
print(soup.find_all(class_='list-small'))

# text 传入的形式可以使字符串或者正则表达式
print(soup.find_all(text=re.compile('Foo')))


## find 返回第一个匹配的几点元素，类型依然是Tag类型
# find_parents() find_parent()
# find_next_siblings()  find_next_sibling
# find_previous_siblings()  find_previous_sibling()
