import pymysql

db = pymysql.connect(host='localhost', user='root', password='880508', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database versio:', data)
# 创建数据库
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")

# sql1 = 'create table if not exists books (id int not null auto_increment,name varchar(50) not null,writer varchar(50),score varchar(8),people varchar(20),info varchar(255),image varchar(255),primary key (id));'
# cursor.execute(sql1)

data = {
    'name': '你不知道的JavaScript（上卷） 在豆瓣购买 去看电子版',
    'writer': '[美] Kyle Simpson / 赵望野、梁杰 / 人民邮电出版社 / 2015-4 / 49.00元',
    'score': '9.4',
    'people': '(595人评价)',
    'info': 'JavaScript语言有很多复杂的概念，但却用简单的方式体现出来（比如回调函数），因此，JavaScript开发者无需理解语言内部的原理，就能编写出功能全...',
    'image': 'https://img3.doubanio.com/view/subject/m/public/s28033372.jpg',
}
table = 'books'
keys = ','.join(data.keys())
print(keys);
values = ','.join(["%s"] * len(data))
print(values)
sql2 = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
print(sql2)
print(tuple(data.values()))
try:
    if cursor.execute(sql2, tuple(data.values())):
        print('success')
        db.commit()
except:
    print('failes')
    db.rollback()


db.close()