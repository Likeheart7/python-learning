import random

from data import *


def main():
    computer_cards = []
    user_cards = []
    # 开始
    start()
    # 开局发牌
    deal_card(computer_cards, user_cards, cur_round=1)
    while True:
        # 展示
        show_cards(computer_cards, user_cards)
        # computer的点数小于17时，自动选择加牌。否则不加牌
        if sum(computer_cards) < 17:
            deal_card(computer_cards)
            print('computer选择加牌')
        # user加牌
        inp = input("你需要加牌嘛？y or n: ")
        if inp == 'y':
            deal_card(user_cards)
            print("你选择加牌。")
        elif inp == 'n':
            # 如果用户不加牌且computer点数大于16，游戏结束
            if sum(computer_cards) > 16:
                break
    check_result(computer_cards, user_cards)
    # print(len(cards))   # 检查一下牌堆的牌数量是否正确


def start():
    print(banner)
    input("回车开始游戏")


# 给每个参与者发两张牌
def deal_card(*card_list, cur_round=0):
    # 如果是第一轮，给每个人发两张牌
    if cur_round == 1:
        for _ in range(2):
            for c in card_list:
                selected = random.choice(cards)
                c.append(selected)
                # 每次取出牌，从牌堆中移除该数字的牌
                cards.remove(selected)
    # 默认给每个人发一张牌
    else:
        for c in card_list:
            selected = random.choice(cards)
            c.append(selected)
            cards.remove(selected)


def check_result(computer_cards, user_cards):
    print("computer 的牌是", computer_cards)
    print("user 的牌是", user_cards)
    # 如果computer爆点了，那么尝试将A当作1点处理
    while sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    # 对user做相同处理
    while sum(user_cards) > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
    # 如果computer点数爆了，根据user点数是否超出确认结果
    if sum(computer_cards) > 21:
        if sum(user_cards) > 21:
            print("It is a draw, you are all over 21!!")
        else:
            print("You win, computer is over 21!!")
    else:
        # 如果computer点数没超过21， 根据用户点数是否超过21处理
        if sum(user_cards) > 21:
            print("You lost, you are over 21")
        # 如果双方都没超过21，比较点数大小
        else:
            computer_point = sum(computer_cards)
            user_point = sum(user_cards)
            if computer_point == user_point:
                print("it's a draw, you are both", sum(user_cards))
            elif computer_point > user_point:
                print(f"Computer win, it's {computer_point}, and you are {user_point}")
            else:
                print(f"You win, you are {user_point}, and computer's point is {computer_point}")


def show_cards(computer_cards, user_cards):
    print(f"computer的底牌是: {computer_cards[0]}")
    print(f"你当前的牌是: {user_cards}, 总点数为{sum(user_cards)}")


if __name__ == '__main__':
    main()
