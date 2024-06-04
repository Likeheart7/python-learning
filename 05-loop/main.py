import random


def loop():
    fruits = ["apple", 'peach', 'pear']
    for fruit in fruits:
        print(fruit)
    for i in range(0, 10, 2):  # [start, end) 左闭右开。step：步长
        print(i)


# 如果数能被3整除，输出fizz，如果能被5整除，输出buzz，如果既能被3整除，又能被5整除，输出fizzbuzz，其余输出数字本身
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


def password_generator():
    password_list = []
    password = ''
    symbols = ['\\', '%', '&', '$', '^']
    numbers = [i for i in range(10)]
    letters = []
    password_length = int(input("你需要多少位的密码？  "))
    symbol_num = int(input("里面有多少个符号？  "))
    number_num = int(input("里面还有多少个数字？  "))

    for i in range(26):
        letters.append(chr(i + 65))
    for i in range(26):
        letters.append(chr(i + 97))
    # print(letters)
    # print(random.choice(letters))   # 随机选一个
    for i in range(symbol_num):
        password_list.append(random.choice(symbols))
    for i in range(number_num):
        password_list.append(random.choice(numbers))
    for i in range(symbol_num + number_num, password_length):
        password_list.append(random.choice(letters))
    random.shuffle(password_list)
    print(password_list)
    password = "".join("%s" % ch for ch in password_list)  # join()遇到非字符串报错
    print(password)


if __name__ == '__main__':
    # loop()
    # fizzbuzz()
    password_generator()