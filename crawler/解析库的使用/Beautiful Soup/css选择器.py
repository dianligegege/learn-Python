from bs4 import BeautifulSoup

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

# 调用select()，传入相应的css选择器
print(soup.select('.panel')) 
print(soup.select('.panel .panel-body')) # 这样写相当于css选择器的交集选择器即 .panel.panel-body
print(soup.select('ul li'))

print('xxx'*30)

# 嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))

print('xxx'*30)

# 获取文本 get_text()
for li in soup.select('li'):
    print('get text:',li.get_text())
