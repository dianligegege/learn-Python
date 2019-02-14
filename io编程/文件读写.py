f = open('/Users/zhangli/Documents/md/API.md','r')

print(f.read(100))

f.close()

with open('/Users/zhangli/Documents/md/API.md','r') as f1:
    print(f1.readline())

# 二进制文件
# with open('User/zhangli/Documents/截图/img1.png','rb') as f2:
#     print(f2.read())

# 写文件
with open('/Users/zhangli/Documents/md/API.md','a') as f2:
    print(f2.write('我是write进来的'))