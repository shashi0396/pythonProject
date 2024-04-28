# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('images.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


# created a list from the extracted list of colors from images.jpeg
import turtle as turtle_module
import random

color_list = [(246, 241, 235), (248, 241, 245), (239, 246, 242), (239, 242, 247), (203, 162, 114), (145, 77, 53),
              (218, 202, 142), (64, 101, 129), (165, 150, 51), (134, 33, 22), (53, 117, 90), (199, 92, 72),
              (137, 161, 180), (75, 39, 31), (145, 178, 149), (34, 57, 73), (230, 176, 165), (163, 143, 156),
              (24, 90, 72), (103, 75, 79), (93, 144, 133), (148, 16, 20), (181, 204, 177), (21, 86, 89), (42, 65, 89),
              (14, 71, 60), (87, 139, 158), (216, 177, 183), (177, 95, 97), (101, 127, 159)]

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
# tim.penup()
# tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
