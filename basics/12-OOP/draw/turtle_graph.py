import random
from turtle import Turtle, Screen
from time import sleep


def draw_square():
    # 直行100
    for _ in range(4):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        # 右转90度
        turtle.right(90)

    turtle.onclick(turtle.goto)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def rand_painting():
    turtle.pensize(10)
    while True:
        turtle.color(rand_color())
        turtle.forward(random.randint(30, 60))
        turtle.right(random.choice([90, 180, 270, 360]))
        sleep(0.2)


def draw_circle():
    turtle.speed(0) # 绘制速度
    amount = 360
    while amount > 0:
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.circle(100)
        turtle.right(5)
        amount -= 5


if __name__ == '__main__':
    turtle = Turtle()
    turtle.shapesize(2, 2, 3)
    screen = Screen()
    screen.colormode(255)
    turtle.shape("turtle")
    # draw_square()
    # rand_painting()
    draw_circle()
