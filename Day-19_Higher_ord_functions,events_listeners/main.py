from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)  # function passed as an 'arguement' to another function. we don't
# use parenthesis, because parenthesis triggers the function to happen to there and then , but here, only when the
# "condition is met, function is triggered". 'keyword-arguement'('kwargs') is used mostly, as positional doesn't make
# sense in most cases.
screen.exitonclick()


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# higher order function

def h_func(n1, n2, func):
    return func(n1, n2)


result = h_func(2, 3, add)  # function as a input
print(result)
