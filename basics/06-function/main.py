def func(arg):
    print("this is a plain function, I accept an arg:", arg)


def accept_func(fun):
    fun("as a argument")


# 可变参数 *】
def multi_args(*args):
    print(args)  # ('a', 1, 3, 4)


if __name__ == '__main__':
    func("this is an arg")
    accept_func(func)  # 将方法作为参数传递
    print(type(func))  # <class 'function'>
    multi_args("a", 1, 3, 4)