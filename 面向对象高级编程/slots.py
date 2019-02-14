class Student(object):
    # 只允许子实例绑定以下两个属性
    __slots__ = ('name','age')

s = Student()
s.name = 'dianli'
s.age = 14
# s.sex = 'nan' 报错