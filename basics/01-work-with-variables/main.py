import sys


def func():
    print("Welcome to the Band Name Generator.")
    city = input("What's name of the city you grew up?\n")
    name = input("What's your pet's name?\n")
    print("Your band name could be", city, name)


def calcLength():
    name = input("what is your name?\n")  # chenxing
    print("Your name has", len(name), "characters")  # 8
    print("Your name take", sys.getsizeof(name), "bytes.")  # 57


def swap():
    a = input("a: ")
    b = input("b: ")
    a, b = b, a
    print("a:", a, "b:", b)


if __name__ == '__main__':
    # func()
    # calcLength()
    swap()
