from pyquery import PyQuery as pq
import requests

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 字符串初始化
doc = pq(html)
print(doc('li'))

# URL初始化
doc1 = pq(url='http://cuiqingcai.com')
doc2 = pq(requests.get('http://cuiqingcai.com').text)
# 两者相等
print(doc1('title'))
print(doc2('title'))

# 文件初始化
doc3 = pq(filename='test.html')
print(doc3('p'))

# 基本css选择器
print(doc('#container .list li')) # 和css一样，和beautiful soup不一样
print(type(doc('#container .list li')))