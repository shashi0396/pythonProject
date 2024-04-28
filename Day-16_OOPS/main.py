# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")  # methods
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)  # attributes i,e in code 'object.attributes'

# timmy is object , 'turtle' is class(blueprint)
# my_screen is object, but we tap into its 'attributes' ie 'canvheight'

# my_screen.exitonclick()
# Methods:-
# Nothing but functions , but tied to objects
# for e.g, color(),shape() are all, 'methods' tied to 'timmy' object under 'Turtle' class

from prettytable import PrettyTable  # 'prettytable' is module/package and 'PrettyTable' is a class

my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])

my_table.align = "l"  # object.attributes

print(my_table.align)

print(my_table)
