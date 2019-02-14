

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log  # 相当于now = log(now)
def now():
    print('2019')

now()

# 1. 运行log(now)，return wraper
#     得到now = def wrapper(*args,**kw):
#             print('call %s():' % now.__name__)
#             return now(*args,**kw)
# 2. 运行wraper函数
#     先打印
#     后返回now函数运行结果，如果没有这个return,则即使now函数有return也只是返回到wrapper函数层级，无法再向上返回



def celebrator(func):
    def inner(*args,**kw):
        print('打印装饰器')
        return func(*args,**kw)
    return inner

@celebrator
def myprint(a):
    return a

@celebrator
def youprint(b):
    print(b)

print(
    myprint(1),
    youprint(2)
)


# 多层嵌套
def get_celebrator(char):
    def print_style(func):
        def inner(*args,**kw):
            print(char*15)
            func(*args,**kw)
        return inner
    return print_style

@get_celebrator('#')
@get_celebrator('*')
def myprint1():
    print('打印一行数据')

myprint1()

# 以下是错误理解，多层和单层不可相提并论
# 1. myprint1 = get_celebrator('#')
#     返回函数  def print_style(myprint1):
#                 def inner(*args,**kw):
#                     print(‘#’ * 15)
#                     myprint1(*args,**kw)
#                 return inner
# 2. 运行myprint1() 
#     返回函数 def inner(*args,**kw):
#                 print(‘#’ * 15)
#                 myprint1(*args,**kw)