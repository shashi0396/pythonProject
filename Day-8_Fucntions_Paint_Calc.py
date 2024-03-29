# your are painting a wall. the instructions on the pain can say a\
# 1 can of paint can cover 5 sq.mtrs of a wall.
# given a random height and width of the wall,
# calculate how many cans of paint you'll need to buy.
import math


def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    round_up_cans = math.ceil(num_of_cans)
    print(f"you'll need {round_up_cans} cans of paint")


test_h = int(input("Enter the height of the wall in 'mts': "))
test_w = int(input("Enter the width of the wall in 'mts': "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
