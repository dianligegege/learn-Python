g1 = (x for x in range(1,5))
print(g1)
print(next(g1),next(g1),next(g1),next(g1))

g2 = (x for x in range(1,5))
# generator可以使用for遍历
for x in g2:
    print(x)

print('分割--------------')

def fib(o):
    n,a,b = 0,0,1
    while n < o:
        print(b)
        a,b = b,a+b
        n = n+1
    print('done')

fib(6)

def fib2(o):
    n,a,b = 0,0,1
    while n < o:
        yield n
        a,b = b,a+b
        n = n+1
    print('done')

print(next(fib2(4)),next(fib2(4)),next(fib2(4)),next(fib2(4)))  # 0 0 0 0

o = fib2(4)
print(next(o),next(o),next(o),next(o)) # 0 1 2 3


for n in fib2(5):
    print(n)

# 练习
# def yh(n):
#     l = [1]
#     while n > 0:
#         l1 = l[:]
#         yield 



