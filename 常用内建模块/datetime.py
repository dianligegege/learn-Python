# datetime

from datetime import datetime,timedelta,timezone
# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))
# 获取指定日期和时间
dt = datetime(2008,1,2,3,4,34)
print(dt,dt.timestamp())
dt1 = datetime(1970,1,1,0,0,1)  # 为负值 即已经包含时区
dt2 = datetime(1970,1,1,8,0,1)  # 1.0
print(dt1,dt1.timestamp())
print(dt2,dt2.timestamp())
# timestamp 转为 datetime
t = 1234567890.0
print(datetime.fromtimestamp(t)) # 转为当地时间
# timestamp 转为带时区datetime
print(datetime.utcfromtimestamp(t)) #转为utc时间
# str转为datetime
cday = datetime.strptime('2015-4-2 12:34:43','%Y-%m-%d %H:%M:%S')
print(cday)
print(cday.strftime('%a, %b %d %H:%M'))

# datetime加减
print(now + timedelta(days=1,hours=3))

# 本地时间转换为utc时间
