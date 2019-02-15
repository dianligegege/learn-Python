

print(
    type(123),
    type('str'),
    type(None),
    type(abs)
)

print(
    type(123) == int,  # true
    type('str') == str, #true
    type('str') == int, #false
)

def fn():
    pass

import types

print(
    type(fn),
    # type(fn) == function 报错
    type(fn) == types.FunctionType # True
)

# instance

print(
    isinstance([1,2,3],(list,tuple)),
    isinstance((1,2,3),(list,tuple))
)

# dir
# 修改默认方法
print(dir('str'))
class Mydog(object):
    def __len__(self):
        return 100
    
    def __dir__(self):
        return '无'

dog = Mydog()
print(
    len(dog),
    dir(dog)
)


# getattr(),setattr(),hasattr()
print(
    hasattr(dog,'x'), # 有无x属性
)
setattr(dog,'x',12)
print(
    getattr(dog,'x'),
    getattr(dog,'y',23),
    getattr(dog,'__dir__')
)


# 实例属性与类属性

class Student(object):

    name = 'dianli'  # 类属性
    def __init__(self,name):
        self.name = name # 实例属性

s = Student('zhangli')
print(
    s.name, # zhangli
    Student.name, # dianli
)

s.name = '张立'

print(
    s.name, # 张立
    Student.name, # dianli
)

del s.name

print(
    s.name, # dianli
    Student.name, # dianli
)

# 练习 没增加一个实例，人数加一

class Student1(object):
    count = 0

    def __init__(self,name):
        Student1.count += 1
        self.name = name

if Student1.count != 0:
    print('测试失败!')
else:
    bart = Student1('Bart')
    if Student1.count != 1:
        print('测试失败!')
    else:
        lisa = Student1('Bart')
        if Student1.count != 2:
            print('测试失败!')
        else:
            print('Student1s:', Student1.count)
            print('测试通过!')