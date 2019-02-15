print(hex(255))

# 位置参数
def power1(x,n):
    s = 1
    while n > 0:
        s = x * s
        n = n - 1
    print(s)

power1(2,5)

# 默认参数
def power2(x,n=2):
    s=1
    while n > 0:
        s = x * s
        n = n - 1
    print(s)

power2(2)


def student(name,age,city='北京',height='120'):
    print('name:',name,'age:',age,'city:',city,'height:',height)

student('zhangli',13)
student('dianli',20)
student('haha',29,height=280,city='河南')
student('adada',44,'上海',190)
student('etgsg',29,height=280)


# 可变参数
def calc1(numbers):
    s = 0
    for n in numbers:
        s = s + n
    print(s)

# list
calc1([1,2,3])
# tuple
calc1((3,4,5))
# 报错
# calc1(1,2,3)

def calc2(*numbers):  # 把一个个参数转为list或turpe
    s = 0 
    for num in numbers:
        s = s + num
    print(s)

calc2(1,2,3)
calc2(*[1,2,3]) # 把list和turpe转为一个一个参数
print(*[1,2,3])  # 1 2 3


# 关键字参数
def person1(name,age,**kw): #把多个键值对转为dict
    print('name:',name,'age:',age,'other:',kw)

# 报错  person1('z',13,'北京')
person1('z',13,city='北京')

extra = {'height':190,'weight':200}
person1('dianili',10,**extra) #把dict转为键值对


# 命名关键字
def person2(name,age,*,height):
    print(name,age,height)
# person2('zhangli',19,**extra) TypeError: person2() got an unexpected keyword argument 'weight'
# person2('zahng',29,height=190,weight=280) TypeError: person2() got an unexpected keyword argument 'weight'
person2('akgf',18,height=190)


#练习题
def product(x,*num):
    s = x
    for n in num:
        s = s * n
    return s
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
