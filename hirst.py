from turtle import Turtle, Screen
import random

colours = ["pink", "orange", "light green", "cornflower blue",
           "medium slate blue", "moccasin", "yellow", "light slate gray"]

tim = Turtle()

tim.up()
tim.goto(-350, 300)


def dot_row():
    tim.dot(20)
    tim.forward(50)


def next_dot_row():
    tim.forward(50)
    tim.dot(20)


for _ in range(5):
    for _ in range(10):
        tim.pencolor(random.choice(colours))
        dot_row()
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    for _ in range(10):
        tim.pencolor(random.choice(colours))
        next_dot_row()
    tim.left(90)
    tim.forward(50)
    tim.left(90)


screen = Screen()
screen.exitonclick()
