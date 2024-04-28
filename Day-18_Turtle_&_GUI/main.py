import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)

# challenge_1: Draw a square

for _ in range(4):
    tim.forward(100)
    tim.right(90)

# challenge_2: Draw a dashed line

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# challenge_3: Drawing different shapes

colours = ["Blue", "Red", "Yellow", "Black"]
directions = [0, 90, 180, 270]


def draw_sides(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3, 11):
    tim.color(random.choice(colours))
    draw_sides(num_sides=sides)

# challenge_4: Generate a random walk

tim.pensize(1)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)  # creating the tuple
    return colour


for _ in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)


# challenge_5: Draw a spirograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_the_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
