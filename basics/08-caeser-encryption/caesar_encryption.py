from data import banner
from data import letter_list

limit = len(letter_list)


def decryption(target, offset):
    result = ''
    for letter in target:
        idx = letter_list.index(letter) - offset
        if idx < 0:
            idx = idx % limit
        result += letter_list[idx]
    print("解密后的结果是:", result)


def encryption(target, offset):
    print(target)
    result = ''
    for letter in target:
        idx = letter_list.index(letter) + offset
        if idx > limit:
            idx %= limit
        result += letter_list[idx]
    print("加密结果是:", result)


def main():
    print(banner)
    while True:
        text = input("输入encode进行加密，输入decode进行解密，输入exit退出程序: ")
        if text == 'encode' or text == 'decode':
            target = input("输入你要处理的字符串: ")
            offset = int(input("输入偏移量: "))
            if offset <= 0:
                print("偏移量需要是一个正整数。")
                continue
        elif text == 'exit':
            break
        else:
            continue
        if text == 'encode':
            encryption(target, offset)
        elif text == 'decode':
            decryption(target, offset)


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("输入的字符串有异常")
