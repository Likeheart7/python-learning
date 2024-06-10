if __name__ == '__main__':
    # 把元组视为一个Record，那么元组的顺序就很有意义
    lax_coordinates = (33.9425, -118.408056)
    print(lax_coordinates)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)
    for country, _ in traveler_ids:
        print(country)

    # 元组作为不可变列表
    items = ('1', 2, [2, 3, 4])
    items2 = tuple(items)
    items[2].append(5)  # 不可变元组的可变元素可以被修改
    print(items)
    print(items2)  # 通过构造器创建的新元组只是一个指向旧元组的新引用，这与list不同
    list1 = [1, 2, 3, [2, 3]]
    list2 = list(list1)  # 通过构造器创建的新list是对原list的拷贝，修改原list不影响新list
    list1.append(4)
    print(list1)
    print(list2)
    list1[3].append(5)  # 当然，这种拷贝是一种浅拷贝，意味着原list中的对象和新list中的持有同一个对象。修改会互相影响
    print(list2)


