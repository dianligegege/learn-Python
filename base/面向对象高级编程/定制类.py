#  __str__ 

class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('dianli'))

# __iter__ 返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 20:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

#  __getitem__ 