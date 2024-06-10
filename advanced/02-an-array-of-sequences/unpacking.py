if __name__ == '__main__':
    print(divmod(20, 4))  # divmod 返回除法的结果和余数
    t = (20, 8)
    quotient, remainder = divmod(*t)
    print(quotient, remainder)

    # 通过*接收剩余值
    a, b, *rest = range(5)
    print(a, b, rest, sep=", ")  # 0, 1, [2, 3, 4]
    a, *rest, b = range(10)
    print(a, rest, b)  # 0 [1, 2, 3, 4, 5, 6, 7, 8] 9    * 前缀可以用于任何位置

    # 嵌套解包
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print(f'{"location":15} | {"latitude":>9} | {"longitude":>9}')  # 15、9表示宽度，>表示右对齐
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

# location        |  latitude | longitude
# Mexico City     |   19.4333 |  -99.1333
# New York-Newark |   40.8086 |  -74.0204
# São Paulo       |  -23.5478 |  -46.6358
