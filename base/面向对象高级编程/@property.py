class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('不是数字')
        if value < 0 or value > 100:
            raise ValueError('超出范围')
        self._score = value

s1 = Student()
s1.set_score(20)
print(s1.get_score())

# 使用@property

class Student1(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('不是数字')
        if value < 0 or value > 100:
            raise ValueError('超出范围')
        self._score = value

s2 = Student1()
s2.score = 80
print(s2.score)


# 练习 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
