import random


def game():
    while True:
        print("------------------- 回合开始 --------------------------")
        val = int(input("请选择你要出什么\n1: ✂\n2: 👊\n3: 🖐️\n"))
        enemy = random.randint(1, 3)
        if val == 1:
            print("你出了✂")
        elif val == 2:
            print("你出了👊")
        elif val == 3:
            print("你出了🖐️")
        else:
            print("你的选择不合适")
            continue
        if enemy == 1:
            print("对方出了✂")
        elif enemy == 2:
            print("对方出了👊")
        elif enemy == 3:
            print("对方出了🖐️")
        if val == 1 and enemy == 1 or val == 2 and enemy == 2 or val == 3 and enemy == 3:
            print("平局")
        elif val == 1 and enemy == 3 or val == 2 and enemy == 1 or val == 3 and enemy == 2:
            print("你赢了")
        else:
            print("你输了")

if __name__ == '__main__':
    game()
