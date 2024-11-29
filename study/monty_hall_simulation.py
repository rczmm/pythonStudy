import random


def monty_hall_simulation(num_simulations: int):
    """
    模拟蒙提霍尔问题

    Args:
      num_simulations: 模拟次数

    Returns:
      float: 换箱子获胜的概率
    """
    win_count_switch = 0
    for _ in range(num_simulations):
        # 初始化三个箱子，其中一个有金币
        doors = [0, 0, 1]
        random.shuffle(doors)

        # 初始选择
        first_choice = random.randint(0, 3)

        # 主持人打开一个空的箱子
        host_choice = [i for i in range(3) if i != first_choice and doors[i] == 0]
        host_choice = random.choice(host_choice)

        # 切换选择
        new_choice = [i for i in range(3) if i not in [first_choice, host_choice]][0]

        # 判断是否获胜
        if doors[new_choice] == 1:
            win_count_switch += 1
            # print(f"换箱子获胜，新选择为：{new_choice}")

    return win_count_switch / num_simulations


# 设置模拟次数
num_simulations = 100

# 进行模拟并输出结果
probability_switch = monty_hall_simulation(num_simulations)
print(f"换箱子获胜的概率约为：{probability_switch:.4f}")
