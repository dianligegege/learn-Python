print(list(range(2,5)))

L = []
for x in range(1,11):
    L.append(x*x)
print(L)

l2 = [x*x for x in range(1,11)]
print(l2)

print([x*x for x in range(1,11) if x %2 ==0])

# 双层循环
print([m+n for m in 'ABC' for n in 'abc'])

l = {1:'a',2:'b',3:'c',4:'5'}
print([(k,v) for k,v in l.items()])


# 练习
l3 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in l3 if isinstance(x,str)]
print(l2)