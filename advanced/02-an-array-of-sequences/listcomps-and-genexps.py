# 列表推导式和生成表达式 list comprehension & generator expression
import array


def listcomps():
    symbols = "%&@#$"
    codes = [ord(c) for c in symbols]  # 列表推导式
    print(codes)
    # 通过lambda实现
    result = list(filter(lambda x: x, map(ord, symbols)))
    print(result)

    # 列表推导式的笛卡尔积
    colors = ['white', 'black']
    sizes = ['S', 'M', 'L']
    tshirt = [(color, size)
              for color in colors
              for size in sizes]
    print(tshirt)  # [('white', 'S'), ('white', 'M'), ('white', 'L'), ('black', 'S'), ('black', 'M'), ('black', 'L')]


def genexps():
    # 生成器表达式用的是括号,通过迭代器协议逐个生成对象
    symbols = '@#$&^'
    codes = tuple(ord(symbol) for symbol in symbols)
    print(codes)
    arr = array.array('I', (ord(symbol) for symbol in symbols))  # 第一个参数表示数组中的类型
    print(arr)
    colors = ['white', 'black']
    sizes = ['S', 'M', 'L']
    # 生成器表达式逐个生成项目，逐个提供，这段代码里从未生成一个 2 * 3 = 6个元素的集合
    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)


if __name__ == '__main__':
    listcomps()
    genexps()
