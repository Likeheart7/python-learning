def main():
    dic = {}
    dic['chen'] = 'xing'
    dic['name'] = 'like'
    dic['day'] = 3
    print(dic)
    print(dic.pop('name'))  # like
    print(dic.keys())  # dict_keys(['chen', 'day'])
    print(dic.get("abc"))  # None
    print(dic.items())  # dict_items([('chen', 'xing'), ('day', 3)])
    for key, value in dic.items():
        print(key, value)
    for item in dic.keys():
        print(item)

    # 嵌套数组
    arr = [1, [2, 3], [4, [5, 6]]]
    print(arr[1][0])  # 2
    print(arr[2][1][0])  # 5


if __name__ == '__main__':
    main()
