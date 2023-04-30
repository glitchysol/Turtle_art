from turtle import Turtle, Screen, colormode
import random

colormode(255)
screen = Screen()
screen.setup(width=1200, height=1000)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def draw_square(turtle_name, num):
    for a in range(4):
        turtle_name.forward(num)
        turtle_name.right(90)


def draw_dotted_line(turtle_name, length):
    for _ in range(length):
        turtle_name.forward(10)
        turtle_name.up()
        turtle_name.forward(10)
        turtle_name.down()


def pyramid(turtle_name):
    for x in range(1, 100, 5):
        draw_square(turtle_name, num=x)


def dotted_shape(turtle_name):  # change right turn to change shape
    for x in range(100):
        turtle_name.forward(x)
        turtle_name.up()
        turtle_name.forward(x)
        turtle_name.down()
        turtle_name.forward(x)
        turtle_name.right(90)


def random_turn(turtle_name):
    turns = [90, 180, 0, 270]
    turtle_name.setheading(random.choice(turns))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk(turtle_name):
    turtle_name.width(10)
    turtle_name.speed("fastest")
    for _ in range(500):
        turtle_name.pencolor(random_color())
        turtle_name.forward(30)
        random_turn(turtle_name)


def spirograph(turtle_name):
    heading = 0
    circle_size = 100
    turtle_name.setheading(heading)
    turtle_name.speed("fastest")
    for _ in range(75):
        # turtle_name.pencolor(random_color())
        turtle_name.circle(circle_size)
        turtle_name.setheading(heading)
        heading += 5
        circle_size += 3


start = -100
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=0, y=start)
    start += 45
    new_turtle.down()
    all_turtles.append(new_turtle)

red = all_turtles[0]
orange = all_turtles[1]
yellow = all_turtles[2]
green = all_turtles[3]
blue = all_turtles[4]
purple = all_turtles[5]

for turtles in all_turtles:
    turtles.speed("fastest")
    turtles.hideturtle()
    counter = 1000
    for turtle in range(100):
        draw_square(turtles, counter)
        random_turn(turtles)
        counter -= 10


spirograph(red)
orange.setheading(90)
spirograph(orange)
yellow.setheading(180)
spirograph(yellow)
green.setheading(270)
spirograph(green)
spirograph(blue)
purple.setheading(90)
spirograph(purple)



screen.exitonclick()
