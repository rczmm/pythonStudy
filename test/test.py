import time


def timer(func):
    """装饰器：计算函数执行时间"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间：{end_time - start_time} 秒")
        return result

    return wrapper


def fibonacci(n):
    """生成器：生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@timer
def generate_fib_squares(n):
    """生成器表达式：生成斐波那契数列的平方"""
    return (x ** 2 for x in fibonacci(n))


def count_up(start=0):
    x = start
    while True:
        yield x
        x += 1


counter = count_up(10)
print(next(counter))  # 输出 10
print(next(counter))  # 输出 11

if __name__ == "__main__":
    # 列表生成式：创建一个列表，包含斐波那契数列的前10个平方
    fib_squares = [x ** 2 for x in fibonacci(10)]
    print(fib_squares)

    # 迭代器：迭代斐波那契数列的前5个平方
    fib_squares_iter = generate_fib_squares(5)
    for x in fib_squares_iter:
        print(x)

    # 装饰器：计算生成斐波那契数列平方的函数执行时间
    generate_fib_squares(10000)
