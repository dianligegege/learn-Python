class Student(object):

    def __init__(self,name,score,sex):
        self.name = name
        self.score = score
        # 私有变量
        self.__sex = sex

    def print_score(self):
        print('%s分数为%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            print('a')
        elif self.score >= 60:
            print('b')
        else:
            print('c')

    # 获取私有变量
    def get_sex(self):
        return self.__sex

    # 设置私有变量
    def set_sex(self,sex):
        if sex == '男':
            self.__sex = '男'
        elif sex == '女':
            self.__sex = '女'
        else:
            raise ValueError('bad sex')

s1 = Student('张立',99,'男')
print('%s分数:%s' % (s1.name,s1.score))
s1.print_score()
s1.get_grade()

# print(s1.__sex)  'Student' object has no attribute '__sex'
s1.__sex = '中性'
print(s1.__sex) # 这个是设置了另一个sex
print(s1.get_sex()) 

s1.set_sex('女')
print(s1.get_sex())
# s1.set_sex('haha')  报错





