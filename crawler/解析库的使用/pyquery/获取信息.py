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

a = doc('.item-0.active a')
# 结果相同
print(a.attr('href'))
print(a.attr.href)

# 如果结果为多个，则获取属性只会获取第一个节点的
a1 = doc('a')
print(a1.attr.href)
# 要想获取多个，可以使用遍历(别忘了使用items())
for item in a1.items():
    print(item, type(item))


### 获取文本

# text() 获取所有子孙节点的文本内容,结果为字符串类型
print(doc('li').text())
print(type(doc('li').text())) 

# html() 只会获取符合条件的第一项,结果为字符串
print(doc('li').html(), type(doc('li').html()))
# 使用遍历 获取全部
for i in doc('li').items():
    print(i.html())
