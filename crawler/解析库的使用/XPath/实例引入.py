from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul>
</div>
'''
# 最会一个li没有闭合会自动修复
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

# 或者直接引入文件
html1 = etree.parse('test.html')
re1 = etree.tostring(html1)
print(re1.decode('utf-8'))