import math


def func():
    sentence = "Hello"
    print(sentence[2])  # l
    print(sentence[-1])  # o
    num = input("Enter a number: ")
    print(int(num))
    res = 8 / 3
    print(round(res, 2))  # round是一个全局方法
    print(math.floor(res))  # math模块有ceil和floor等方法


def calc_tips():
    total = float(input("这次聚会一共花了多少元？￥ "))
    count = int(input("这次一共有多少人参加？"))
    extra = float(input("额外消费了多少？% "))
    print("每个人这次需要支付", total * (1 + extra / 100) / count, "元")


def calc_time_remaining():
    age = int(input("你现在多少岁?\n"))
    year_remaining = 90 - age
    month_remaining = year_remaining * 12
    week_remaining = year_remaining * 52
    day_remaining = year_remaining * 365
    print(f'You have {day_remaining} days, {week_remaining} weeks, and {month_remaining} months left')


if __name__ == '__main__':
    # func()
    # calc_tips()
    # print(6 / 3)  # 2.0  除法的结果是浮点数
    # print(8 // 3)  # 2  结果是int，截断小数
    calc_time_remaining()
