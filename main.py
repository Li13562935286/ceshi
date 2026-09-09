# -*- coding: utf-8 -*-
"""猜数字小游戏

电脑会随机想一个 1 到 100 之间的整数，你在终端里输入数字来猜。
每猜一次，程序会提示"大了"还是"小了"，直到猜中为止。

运行方式（在终端中）：
    python main.py
"""

import random


def main():
    print("=" * 30)
    print("欢迎来玩猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的整数。")
    print("=" * 30)

    answer = random.randint(1, 100)  # 随机生成答案
    tries = 0  # 记录猜了多少次

    while True:
        tries += 1

        # 读取玩家输入，并处理"输入的不是数字"的情况
        try:
            guess = int(input(f"第 {tries} 次猜测，请输入一个整数: "))
        except ValueError:
            print("输入的不是数字，这次不算，请重新输入。")
            tries -= 1
            continue

        if guess < answer:
            print("太小了，再大一点～")
        elif guess > answer:
            print("太大了，再小一点～")
        else:
            print(f"恭喜你！猜对了，答案就是 {answer}，一共用了 {tries} 次。")
            break


if __name__ == "__main__":
    main()
