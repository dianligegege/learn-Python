# 切片
l = [1,2,3,4,5,6]
print(l[0:3]) # [1,2,3]
print(l[:3]) # [1,2,3]
print(l[0:7]) # [1, 2, 3, 4, 5, 6]
print(len(l[0:7])) # 长度为6
print(l[1:2]) # [2]
print(l[2:1]) # [] 前一位在后一位的右边为空
print(l[-2:-1]) # [5]

# 练习
def trim(s):
    flag =True
    for word in s:
        if word != ' ':
            flag = False
    if flag:
        return ''
    while s[0] == ' ' and len(s)>0:
        s=s[1:]
    while s[-1] == ' ' and len(s)>0:
        s = s[:-1]
    return s
trim('  hello')
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')