#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 导入模块
import json

# json.loads json字符串 转 Python数据类型
json_string = '''
{
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
'''

# json字符串 转 dict
print("json字符串 转 dict")
print(type(json_string))
data = json.loads(json_string)
print(type(data))
print(data)

# json文件 转 dict
print("json文件 转 dict")
with open('data.json',"r",encoding='utf-8') as f:
    data = json.load(f)
    print(type(data))
    print(data)

data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}

# dict 转 json字符串
print("dict 转 json字符串")
# ensure_ascii = False 可以防止中文转化问题
# indent 设置tab大小
json_string = json.dumps(data,ensure_ascii = False,indent = 4)
print(type(json_string))
print(json_string)

# dict 转 json文件
print("dict文件 转 json字符串")
with open("dat.json","w",encoding = 'utf-8') as f:
    json.dump(data,f,ensure_ascii = False,indent = 4)

