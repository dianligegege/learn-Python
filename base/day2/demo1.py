import math

def fun1(x):
    if x >= 0:
        return x
    else:
        return -x
print(fun1(-3))

def qua(a, b, c):
    if not isinstance(a,(int,float)) and isinstance(b,(int,float))and isinstance(c,(int,float)):
        raise TypeError ('格式不对')
    elif b*b-4*a*c>0:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return ((x1,x2))
    else:
        return('无解')

print(qua(2,3,1))

def fun2(l=[]):
    l.append('end')
    print(l)

fun2()
fun2()

def fun3(l=None):
    if l is None:
        l =[]
    l.append('end')
    print(l)

fun3()
fun3()

def fun4(num):
    sum=0
    for n in num:
        sum = sum+n*n
    print(sum)

fun4([1,2,3])

def fun5(*num):
    sum=0
    for n in num:
        sum = sum+n*n
    print(sum)

fun5(1,2,3)
fun5(*[1,2,3])

def fun6(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

fun6('zhangli',14,city='beijing')
extra = {'city':'henan'}
fun6('hh',34,**extra)

def fun7(name,age,*,city='beijing',jop):
    print(name,age,city,jop)

fun7('zhangli',38,jop='coder')

def fun8(x):
    if x == []:
        return (None,None)
    if len(x) == 1:
        return(x[0],x[0])
    max=x[0]
    min=x[0]
    for item in x:
        if item < min:
            min = item
        if item> max:
            max = item
    return (min,max)

if fun8([]) != (None, None):
    print('测试失败!')
elif fun8([7]) != (7, 7):
    print('测试失败!')
elif fun8([7, 1]) != (1, 7):
    print('测试失败!')
elif fun8([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


L=[m+n for m in 'abc' for n in 'awd']
print(L)
