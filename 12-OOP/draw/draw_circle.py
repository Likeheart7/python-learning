from turtle import Turtle, Screen

from color_extract import extract_color


def draw():
    colors = extract_color('image.jpg', 36)
    print(len(colors))
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.speed(0)
    screen = Screen()
    screen.colormode(255)
    for i in range(36):
        turtle.color(colors[i])
        turtle.circle(100)
        turtle.right(10)
    screen.exitonclick()


if __name__ == '__main__':
    draw()