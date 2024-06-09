members = []
members.append("cehnxing")
members.append("likeheart")
members.insert(0, 'lius')
cities = ['huainan', 'hefei', 'anqing','fuyang','bozhou']
members[len(members):] = cities  # 代替extends()的一种方式
print(members)

