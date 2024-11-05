import random
import copy
from collections import Counter
from itertools import groupby
from itertools import islice
from functools import reduce

# 定义一个列表
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成随机数 列表解析式（列表生成式）
# random.randint(1, 100) 生成1-100之间的随机数
list_range = [random.randint(1, 100) for i in range(100)]

# 遍历列表 输出索引和值 range是一个左闭右开区间
# 0 起点索引 1 步长（默认为1）
for i in range(0, len(list_data), 1):
    print(i)
    print(list_data[i])

# 遍历列表 输出值
for i in list_data:
    print(i)

# 使用 enumerate 遍历索引和值
for index, value in enumerate(list_data):
    print(f"Index: {index}, Value: {value}")

# 1. 添加元素
# append 方法在列表末尾添加一个元素
list_data.append(11)

# insert 方法在指定位置插入一个元素
list_data.insert(0, 0)

# 2. 删除元素
# remove 方法删除第一个匹配的元素
list_data.remove(0)

# pop 方法删除指定索引位置的元素
list_data.pop(0)

# index 方法返回第一个匹配元素的索引，如果不存在则抛出 ValueError
index_of_5 = list_data.index(5)

# count 方法返回指定元素在列表中出现的次数
count_of_5 = list_data.count(5)

# sort 方法对列表进行原地排序，默认是升序
list_data.sort()

# 使用 key 参数指定排序的规则,绝对值
list_data.sort(key=abs)

# 使用 reverse_sorted 参数对列表进行原地逆向排序
list_data.sort(reverse=True)

print(list_data)

# reverse 方法对列表进行原地反转
list_data.reverse()

# 切片反转
reversed_list = list_data[::-1]

# 切片操作可以获取列表的一部分
sub_list = list_data[2:5]  # 获取索引 2 到 4 的元素

last_three = list_data[-3:]  # 获取最后三个元素

every_second = list_data[::2]  # 获取每隔一个元素 步长切片

# copy 方法返回列表的一个浅拷贝
copied_list = list_data.copy()

# 深拷贝
deep_copied_list = copy.deepcopy(list_data)

# clear 方法清空列表
list_data.clear()

# 生成一个平方数列表
squares = [x ** 2 for x in range(10)]

# 生成一个偶数列表
evens = [x for x in range(10) if x % 2 == 0]

# 使用加法合并两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # 使用 extend 方法
merged_list = list1 + list2

# 使用 join 方法拼接字符串列表
string_list = ['a', 'b', 'c']
joined_string = ''.join(string_list)

# 使用 len 函数获取列表的长度
length = len(list_data)

# 使用 max 和 min 函数获取列表的最大值和最小值
max_value = max(list_data)
min_value = min(list_data)

# 使用 sum 函数计算列表的总和
sum_value = sum(list_data)

# 将列表中的每个元素平方
squared = list(map(lambda x: x ** 2, list_data))

# 使用 filter 函数过滤列表
evens_list = list(filter(lambda x: x % 2 == 0, list_data))

# 使用集合去重
unique_list = list(set(list_data))

# 使用 split 方法将字符串分割成列表
string_list = "apple,banana,cherry".split(',')

# 使用 zip 函数将两个列表组合成一个元组列表
zipped = list(zip(list1, list2))

# 解压
list1, list2 = zip(*zipped)

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 使用列表解析式分组
grouped = [list_data[i:i + 3] for i in range(0, len(list_data), 3)]

# 列表的计数
counter = Counter(list_data)

list_data = [1, 1, 2, 2, 3, 3, 4, 4]
list_data.sort()  # 先排序
grouped_data = {k: list(v) for k, v in groupby(list_data)}

# 切片旋转
list_data = [1, 2, 3, 4, 5]
k = 2  # 旋转步长
rotated = list_data[-k:] + list_data[:-k]

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced = list(islice(list_data, 2, 8, 2))  # 从索引2开始，每2个元素取一个，直到索引8

list_data = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, list_data)
