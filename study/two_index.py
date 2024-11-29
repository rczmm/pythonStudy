# -*- coding: utf-8 -*-
"""
@desc: 双指针的简单应用·
"""
import random
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start}")
        return result

    return wrapper


@count_time
def two_sum(numbers: list, target: int) -> (int, int):
    """两数之和"""
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return left + 1, right + 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


@count_time
def remove_val(numbers: list, val: int) -> list:
    """移除数组中的指定值"""
    left = 0
    right = len(numbers) - 1
    while left <= right:
        if numbers[left] == val:
            numbers[left] = numbers[right]
            right -= 1
        else:
            left += 1
    return numbers[:left]


@count_time
def merge_list(numbers1: list, numbers2: list) -> list:
    """合并两个有序数组"""
    i = j = 0
    result = []
    while i < len(numbers1) and j < len(numbers2):
        if numbers1[i] < numbers2[j]:
            result.append(numbers1[i])
            i += 1
        else:
            result.append(numbers2[j])
            j += 1
    result.extend(numbers1[i:])
    result.extend(numbers2[j:])
    return result


@count_time
def is_reverse(string: str) -> bool:
    """判断是否是回文串"""
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


@count_time
def is_exist(string: str, val: str) -> bool:
    """判断字符串中是否存在指定字符"""
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == val or string[right] == val:
            return True
        left += 1
        right -= 1
    return False


if __name__ == '__main__':
    two_sum(numbers=[2, 7, 11, 15], target=13)
    remove_val(numbers=[random.randint(0, 10) for _ in range(100000)], val=random.randint(0, 10))
    merge_list(numbers1=[random.randint(0, 10) for _ in range(100000)],
               numbers2=[random.randint(0, 10) for _ in range(100000)])
    is_reverse(string='a' * 10000 + 'b' * 100000 + 'c' * 100 + 'd' * 100 + 'a' * 10000)
    is_exist(string='a' * 10000 + 'b' * 100000 + 'c' * 100 + 'd' * 100 + 'a' * 10000, val='b')
