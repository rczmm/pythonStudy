import json
from datetime import datetime

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 将 Python 对象转换为 JSON 字符串
# 使用 json.dumps 方法
json_str = json.dumps(data)

# 将 JSON 字符串转换为 Python 对象
# 使用 json.loads 方法
json_str = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_str)

# 将 Python 对象写入 JSON 文件
# 使用 json.dump 方法
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# 从 JSON 文件读取 Python 对象
# 使用 json.load 方法
with open('data.json', 'r') as file:
    data = json.load(file)


# 处理复杂数据类型
# 自定义编码器
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)


data = {
    "name": "Alice",
    "age": 25,
    "hobbies": {"reading", "traveling", "coding"}
}

json_str = json.dumps(data, cls=CustomEncoder)


# 自定义解码器
def custom_decoder(dct):
    if 'hobbies' in dct:
        dct['hobbies'] = set(dct['hobbies'])
    return dct


json_str = '{"name": "Alice", "age": 25, "hobbies": ["reading", "traveling", "coding"]}'
data = json.loads(json_str, object_hook=custom_decoder)


# 处理日期和时间
# 编码日期
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


data = {
    "name": "Alice",
    "age": 25,
    "birthdate": datetime(1998, 5, 20)
}

json_str = json.dumps(data, cls=DateTimeEncoder)


# 解码日期
def datetime_decoder(dct):
    if 'birthdate' in dct:
        dct['birthdate'] = datetime.fromisoformat(dct['birthdate'])
    return dct


json_str = '{"name": "Alice", "age": 25, "birthdate": "1998-05-20T00:00:00"}'
data = json.loads(json_str, object_hook=datetime_decoder)

# 处理嵌套 JSON
# 编码嵌套 JSON
data = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

json_str = json.dumps(data, indent=4)

# 解码嵌套 JSON
json_str = '{"name": "Alice", "age": 25, "address": {"street": "123 Main St", "city": "New York", "state": "NY"}}'
data = json.loads(json_str)

# 处理 JSON 数组
# 编码数组
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

json_str = json.dumps(data, indent=4)

# 解码数组
json_str = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]'
data = json.loads(json_str)

# 处理 JSON 错误
# 捕获 JSON 解析错误
try:
    json_str = '{"name": "Alice", "age": 25, "invalid": }'
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
# 输出: JSON Decode Error: Expecting property name enclosed in double quotes: line 1 column 31 (char 30)
# 处理 JSON 在网络请求中的应用
# 发送 JSON 数据
import requests

url = "https://api.example.com/data"
data = {
    "name": "Alice",
    "age": 25
}

response = requests.post(url, json=data)
print(response.status_code)  # 输出: 200
print(response.json())  # 输出: {'message': 'Data received successfully'}

# 接收 JSON 数据
url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)  # 输出: {'name': 'Alice', 'age': 25}
else:
    print(f"Request failed with status code: {response.status_code}")

# 处理 JSON 在文件中的应用
# 写入 JSON 数据到文件
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# 读取 JSON 数据从文件
with open('data.json', 'r') as file:
    data = json.load(file)
