from functools import reduce

def list(x):
    l = []
    for n in x:
        l.append(n)
    print(l)


l1 =[1,2,3,4,5,6]

# map
def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6])
print(r)
list(r)

list(map(str,l1))

# reuce
# 求和
def he(x,y):
    return x+y
print(reduce(he,l1))

# 字符串转数字 int()
def tolist(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
def tonum(x,y):
    return x*10 + y
print(reduce(tonum,map(tolist,'123456')))

# 练习 把不规范的名字转规范，即首字母大写
def normalize(name):
    name =  name[0].upper()+name[1:].lower()
    return name
list(map(normalize,['adam', 'LISA', 'barT']))

# 求积
def prod(x,y):
    return x*y
print(reduce(prod,[3,5,7,9]))

# 字符串转浮点数
# def str2float(s):
#     dig = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}
#     return dig[s]

# list(map(str2float,'123.456'))

# def toint(x,y):
#     if y != '.':
#         return x*10 + y
#     else:

# print(reduce(tonum,map(str2float,'123.456')))

# filter
def odd(x):
    return x%2==0
f1 = filter(odd,l1)
print(f1)
print(next(f1))
list(f1)  # for循环对于Iterator相当于next()

# sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def byname(t):
    return str.lower(t[0])

def byscore(t):
    return t[1]

l2 = sorted(L,key=byname)
print(l2)

print(sorted(L,key=byscore))


