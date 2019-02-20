import re

# 匹配目标 match是从头开始匹配
content = 'hello 2424424 aihiahg iahlahg ogah afh'
result = re.match('^hello\s(\d+)\saihiahg', content)
print(result)
# 匹配内容
print(result.group())
# 匹配到的内容里第一个小括号里的内容
print(result.group(1))
# 匹配到的范围
print(result.span())

# 修饰符
c1 = '''hello 2234
world'''
# 换行匹配不到
r1 = re.match('^he.*?(\d+).*?world$', c1)
print(r1)

# 加修饰符 S匹配换行符 I大小写不敏感 M多行匹配
r2 = re.match('^he.*?(\d+).*?world$', c1, re.S)
print(r2)
print(r2.group(1))

# search 相当于js的match
# match匹配不到
r3 = re.match('\d+', c1)
print(r3)
# 用search可以匹配到
r4 = re.search('\d+', c1)
print(r4)

# findall() 获取所有匹配内容
html = '''<div id="songs-list" > <h2 class=气itle"〉经典老歌</h2> <p class="introduction"> 经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐泰">往事随风 </a>
</li>
<li data-view=飞"><a href="/4.mp3" singer="beyond">尤辉岁月 </a></li><li data-view="5"><a href="/S.mp3" singer="除A也琳">记事本</a></li> <li data-view="5">
<a href="/6.mp3" singer="邓丽君、但愿人长久"</a>
</li>
</ul>
</div>'''
r5 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r5)
print(type(r5)) # list类型
for result in r5:
    print(result)
    print(result[0], result[1], result[2])

# compile 构建正则对象
# sub 正则替换
content1 = '2016-12-14 12:00'
content2 = '2017-12-14 16:00'
content3 = '2018-12-14 13:00'
pattern = re.compile('\d{2}:\d{2}')
re1 = re.sub(pattern, '', content1)
re2 = re.sub(pattern, '', content2)
re3 = re.sub(pattern, '', content3)
print(re1, re2, re3)
