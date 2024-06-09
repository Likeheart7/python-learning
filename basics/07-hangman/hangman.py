import random
from graph import *

def hangman():
    words = ['name', 'sentence', 'luck', 'sentinel', 'camel', 'otter']
    health = len(stages)  # 是7，一共允许错六次
    choice_word = random.choice(words)
    display_list = ['_'] * len(choice_word)
    print(banner)

    # 当生命值大于1时一直循环
    while health > 1:
        guess = input("输入你猜测的字母: ")
        if guess not in choice_word:
            health -= 1
            print(stages[-health])  # 出错打印进度
            continue
        for i in range(len(choice_word)):
            letter = choice_word[i]
            if letter == guess:
                display_list[i] = letter
        print(display_list)
        if '_' not in display_list:
            break
    if '_' not in display_list:
        print("you win")
    else:
        print("you lose")


if __name__ == '__main__':
    hangman()
