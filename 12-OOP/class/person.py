from abc import ABC, abstractmethod


class Person(ABC):  # 继承ABC类, 且拥有被@abstractmethod装饰器修饰的方法的自定义类是抽象类，无法实例化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 被@abstractmethod装饰器修饰的是抽象方法，需要子类重写
    @abstractmethod
    def eat(self):
        pass


if __name__ == '__main__':
    person = Person('chen', 25)  # 带有抽象方法的抽象类不能被实例化 Can't instantiate abstract class Person with abstract method eat
