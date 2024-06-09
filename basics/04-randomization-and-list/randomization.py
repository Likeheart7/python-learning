import random

count_list = [0] * 10  # 创建一个长度为10，初始值全为0的列表
for i in range(1000000):
    idx = random.randint(0, 9)  # 闭区间
    count_list[idx] += 1

print(count_list)

rand_float = random.random()  # [0, 1)之间的浮点数
print(rand_float)

random.seed(1, 1)  # 随机种子可以让每一次运行取到的随机数是一样的
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 10))
print(numbers)