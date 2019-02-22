from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)

# 所有节点 //所有子孙节点
r1 = html.xpath('//*')
print(r1)

# 子节点  /直接子节点
r2 = html.xpath('//li/a')
print(r2)

# 父节点与属性匹配 先获取子孙节点中href属性为XXX的a标签，再获取其父节点的class属性值
r3 = html.xpath('//a[@href="link4.html"]/../@class')
print(r3)

# 文本获取
r4 = html.xpath('//li[@class="item-0"]/text()')
print(r4) # 获取不到
r5 = html.xpath('//li[@class="item-0"]/a/text()')
print(r5)
r6 = html.xpath('//li[@class="item-0"]//text()')
print(r6) # 三个结果，包含换行符

# 属性获取
r7 = html.xpath('//li/a/@href')
print(r7)

# 属性多值匹配
text1 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html1 = etree.HTML(text1)
r8 = html1.xpath('//li[@class="li"]/a/text()')
print(r8) # 匹配不到
r9 = html1.xpath('//li[contains(@class,"li")]/a/text()')
print(r9)

# 多属性匹配 
r10 = html1.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(r10)

# 按序选择
# 选择第一个，从1开始
r11 = html.xpath('//li[1]/a/text()')
print(r11)
r12 = html.xpath('//li[last()]/a/text()')
print(r12)
r13 = html.xpath('//li[position()<3]/a/text()')
print(r13)
# 倒数第三个
r14 = html.xpath('//li[last()-2]/a/text()')
print(r14)

# 节点轴选择
# 获取所有祖先节点
r15 = html.xpath('//li[1]/ancestor::*')
print(r15)
# 获取所有祖先节点中的div
r15 = html.xpath('//li[1]/ancestor::div')
print(r15)
# 获取所有属性值
r16 = html.xpath('//li[1]/attribute::*')
print(r16)
# 获取所有子节点
r17 = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(r17)
# 获取所有子孙节点
r18 = html.xpath('//li[1]/descendant::span')
print(r18)
# 获取当前节点之后的所有节点（包括同级和下一级的）,然后父节点和子节点并排排列,所以是li a li a ...
r19 = html.xpath('//li[1]/following::*')
print(r19)
# 获取当前节点之后的所有同级节点,所以是li li li ...
r20 = html.xpath('//li[1]/following-sibling::*')
print(r20)