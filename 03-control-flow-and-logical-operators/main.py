def branch_if():
    val = input("enter red or blue: ")
    if val == "red" and True:
        print("you join the red team.")
    elif val == "blue" or False:
        print("you join the blue team.")
    else:
        print("you can't enter any word other than red or blue.")


def branch_for():
    for i in range(10, 0, -1):
        print(f"there are {i} round")


if __name__ == '__main__':
    branch_if()
    branch_for()
