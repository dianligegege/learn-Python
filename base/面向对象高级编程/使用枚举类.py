from  enum import Enum ,unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# value属性是自动赋给成员的int常量，默认从1开始计数
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

@unique
class Weekday(Enum):
    Sun = 0