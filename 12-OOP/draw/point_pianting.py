import random
from turtle import Turtle, Screen
from color_extract import extract_color


def draw(colors):
    turtle = Turtle()
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.colormode(255)
    turtle.shape('turtle')
    turtle.shapesize(3)
    turtle.pensize(1)
    turtle.penup()
    # 前往起始点
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    for i in range(1, 101):
        turtle.speed(1)
        turtle.showturtle()
        turtle.pendown()
        turtle.dot(20, random.choice(colors))
        turtle.penup()
        if i % 10 == 0:
            turtle.speed(0)
            turtle.hideturtle()
            turtle.left(90)
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(360)
            turtle.left(180)
        else:
            turtle.forward(40)

def main():
    colors = extract_color('./color_palette.jpg', 30)
    draw(colors)


if __name__ == '__main__':
    main()