import json

### 读取json

# json.loads() 字符串转为json格式
str = '''
    [{
        "name": "张立",
        "age": 23
    },{
        "name": "dianli",
        "age": 42
    }]
'''
data = json.loads(str)
print(data)
print(type(data))

# 获取json数据 
print(data[0]['name'])
# 或使用get(),可以传入第二个参数，代表默认值
print(data[0].get('name'))
print(data[0].get('sex', '男')) # 无此属性输出默认值’男‘
print(data[0]) # 但是原对象没有变化


### 输出json

# json.dumps 将json对象转为字符串
with open('data.json', 'a') as file:
    file.write(json.dumps(data))
    # 使用indent设定缩进参数，
    file.write(json.dumps(data, indent=2))

# 输出中文
with open('data.json', 'a', encoding='utf-8') as file1:
    # 使用indent设定缩进参数，
    file1.write(json.dumps(data, indent=2, ensure_ascii=False))