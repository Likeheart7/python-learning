from person import Person


# A simple class
class User(Person):
    # constructor
    def __init__(self, name, age):
        super().__init__(name, age)
        self.follower = 0

    def show(self):
        print(f"name: {self.name}, age: {self.age}, followers: {self.follower}")    # 父类的属性直接继承给子类，通过self调用即可

    def eat(self):
        print("User eat...")
