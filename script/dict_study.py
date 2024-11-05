import copy
from collections import defaultdict, ChainMap
from itertools import groupby

# 使用字面量创建
dict_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 使用 dict 构造函数创建
dict_data = dict(name='Alice', age=25, city='New York')

# 使用键值对列表创建
dict_data = dict([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 通过键访问值
name = dict_data['name']  # 输出: Alice

# 使用 get 方法访问值
name = dict_data.get('name')  # 输出: Alice
unknown = dict_data.get('gender', 'Unknown')  # 输出: Unknown

# 添加键值对
dict_data['email'] = 'alice@example.com'

# 更新键值对
dict_data['age'] = 26

# 删除键值对
del dict_data['age']

# 使用 pop 方法 删除键值对
age = dict_data.pop('age')

# 使用 popitem 方法 删除并返回最后一个键值对
key, value = dict_data.popitem()

# 使用 in 关键字 检查键是否存在
is_exist = 'name' in dict_data

# 遍历键
dict_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in dict_data:
    print(key)

# 遍历值
dict_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for value in dict_data.values():
    print(value)

# 遍历键值对
dict_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in dict_data.items():
    print(f"{key}: {value}")

# 使用 update 方法 合并字典
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'email': 'alice@example.com'}
dict1.update(dict2)

# 使用 {**dict1, **dict2} 语法 合并
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'email': 'alice@example.com'}
merged_dict = {**dict1, **dict2}

# 使用 copy 方法 浅拷贝
dict_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
shallow_copy = dict_data.copy()

# 深拷贝
dict_data = {'name': 'Alice', 'age': 25, 'details': {'city': 'New York'}}
deep_copy = copy.deepcopy(dict_data)

# 使用 len 函数 获取长度
length = len(dict_data)

# 按键排序
dict_data = {'b': 2, 'a': 1, 'c': 3}
sorted_by_key = dict(sorted(dict_data.items()))

# 按值排序
dict_data = {'b': 2, 'a': 1, 'c': 3}
sorted_by_value = dict(sorted(dict_data.items(), key=lambda item: item[1]))

# 使用字典解析式过滤
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in dict_data.items() if v > 2}

# 使用字典解析式映射
dict_data = {'a': 1, 'b': 2, 'c': 3}
mapped = {k: v * 2 for k, v in dict_data.items()}

# 使用 defaultdict
dict_data = defaultdict(int)
dict_data['a'] += 1
dict_data['b'] += 2

# 创建嵌套字典
nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}

# 访问嵌套字典
# 使用 ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)


# 解包字典作为参数
def print_person(name, age):
    print(f"Name: {name}, Age: {age}")


person = {'name': 'Alice', 'age': 25}
print_person(**person)  # 输出: Name: Alice, Age: 25

# 交换键值对
dict_data = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in dict_data.items()}

dict_data = {'a1': 1, 'a2': 2, 'b1': 3, 'b2': 4}
grouped = {k: list(v) for k, v in groupby(dict_data.items(), key=lambda item: item[0][0])}

# 使用 filter 函数
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = dict(filter(lambda item: item[1] > 2, dict_data.items()))

# 使用 map 函数
dict_data = {'a': 1, 'b': 2, 'c': 3}
mapped = dict(map(lambda item: (item[0], item[1] * 2), dict_data.items()))
