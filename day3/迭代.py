from collections.abc import Iterable

# 迭代

d = {'a':1,'b':2,'c':3}
print(d.items())

for k in d:
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,v)

for i in d.items():
    print(i)
    print(isinstance(i, Iterable))


for i, value in enumerate(['a','b','c']):
    print(i,value)

#  练习
def fm(l):
    min = l[0]
    max = l[0]
    for x in l:
        if x > max:
            max = x
        if x < min:
            min =x
    return (min,max)

l = [1,3,2,5,22]
print(fm(l))