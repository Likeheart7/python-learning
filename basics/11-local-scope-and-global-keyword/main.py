def incr_health():
    # 这里定义的是一个函数作用域的health，不是给全局变量赋值
    health = 2
    print(health)


def global_incr():
    # 通过global关键字访问全局变量，然后可以对全局变量做修改
    global health
    health = "health changed"


#  nonlocal 关键字只能在嵌套函数中使用。
#  nonlocal 关键字声明的变量必须存在于最近的封闭作用域中，否则会引发 SyntaxError。
def wrapper():
    live = 1

    def nest():
        nonlocal live  # 使用nonlocal指向，外层函数中定义的变量
        live = 11  # 如果不加nonlocal，指向的是函数作用域变量外层函数的变量

    nest()
    print(live)


# python没有块作用域，只有函数作用域和类作用域
def non_block_scope():
    if True:
        a = 3
    print(a)  # 因为python没有块作用域，所以可以访问到if语句内的a变量


if __name__ == '__main__':
    health = 1
    incr_health()
    print(health)
    global_incr()
    print(health)
    wrapper()
    non_block_scope()
