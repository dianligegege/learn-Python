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
         <div>
            <li id='liid'>我是div里的li</li>
         </div>
     </ul>
 </div>
'''

doc = pq(html)

# 子孙节点
item = doc('.list').find('li') 
print(item)

# 子节点
item1 = doc('.list').children('li')
print(item1)

# 父节点
item2 = doc('#liid').parent() # 小括号里可以加，没啥用
print(item2)

# 祖先节点
item3 = doc('#liid').parents('ul') # 这个小括号写才有意义
print(item3)
print(type(doc('#liid').parents())) # <class 'pyquery.pyquery.PyQuery'>

# 兄弟节点
li = doc('.list .item-0.active')
print(li.siblings('div'))

# 遍历 调用items()方法
li1 = doc('li').items() # 得到一个生成器
for li in li1:
    print(li)

