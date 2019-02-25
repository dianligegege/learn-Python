import csv

# 追加写入改为‘a’
with open('datadict.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})


# 读取
with open('datadict.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)