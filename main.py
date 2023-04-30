from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape("turtle")
colours = ["hot pink", "yellow", "red", "light blue", "blue violet",
           "spring green", "peach puff", "silver", "rosy brown",
           "blue", "black", "aquamarine", "dark orange", "maroon"]
random_rgb = (random.choice(range(1, 256)), random.choice(range(1, 256)), random.choice(range(1, 256)))
colormode(255)


def draw_square(turtle_name, num):
    for a in range(4):
        turtle_name.forward(num)
        turtle_name.right(90)

# print shapes with 3 - 10 sides. each shape a different color
# for x in range(3, 11):
#     timmy.color(random.choice(colours))
#     for _ in range(x):
#         timmy.forward(100)
#         timmy.right(360/x)


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
    for _ in range(200):
        turtle_name.pencolor(random_color())
        turtle_name.circle(circle_size)
        turtle_name.setheading(heading)
        heading += 5
        # circle_size += 1




dotted_shape(timmy)










screen = Screen()
screen.exitonclick()