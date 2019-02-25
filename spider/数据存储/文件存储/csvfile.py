import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 20])
    writer.writerow(['10003', 'Jordan', 20])

# 添加分隔符
with open('data.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 20])
    writer.writerow(['10003', 'Jordan', 20])