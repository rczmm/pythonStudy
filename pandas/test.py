import pandas
import random

data = {
    'line_id': [i for i in range(1, 100)],
    'position_x': [random.randint(0, 100) for x in range(1, 100)],
    'position_y': [random.randint(0, 100) for y in range(1, 100)],
    'position_b': [random.randint(0, 100) for b in range(1, 100)],
    'position_l': [random.randint(0, 100) for l in range(1, 100)],
    'is_deleted': [random.randint(0, 1) for t in range(1, 100)],
    'tenant_id': [random.randint(0, 100) for t in range(1, 100)],
    'gcj_b': [random.randint(0, 100) for b in range(1, 100)],
    'gcj_l': [random.randint(0, 100) for l in range(1, 100)]
}

pd_data = pandas.DataFrame(data)

res = (pd_data
       .query('is_deleted==0')  # 过滤掉已删除的行
       .sort_values(by=['line_id', 'tenant_id'])  # 按 tenant_id 和 line_id 排序
       .reset_index(drop=True)  # 重置索引
       .assign(new_cloumn=lambda x: x['line_id'] + x['tenant_id'])  # 添加新列
       .loc[:, ['line_id', 'position_x', 'position_y', 'position_b']])  # 选择特定列


def catch_exception(func):
    """
    一个装饰器，用于捕获并处理被装饰函数执行过程中可能发生的异常。
    这个装饰器将捕获所有异常，并打印异常信息，避免程序因未处理的异常而崩溃。

    参数:
    - func: 被装饰的函数。

    返回:
    - wrapper: 包装了异常捕获逻辑的函数。
    """

    def wrapper(*args, **kwargs):
        # 尝试执行被装饰的函数。
        try:
            return func(*args, **kwargs)
        # 捕获执行过程中发生的任何异常。
        except Exception as e:
            # 打印异常信息，而不是让程序崩溃。
            print(e)

    return wrapper


@catch_exception
def throw_error():
    raise Exception('我是一个异常')


if __name__ == '__main__':
    throw_error()
