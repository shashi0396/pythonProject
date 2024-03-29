import random

# Taking input as a string using input function
names_string = input("Enter your team member names: ")

names = names_string.split(", ")
# enter names followed by comma then space

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

random_name = names[random_choice]

print(f" {random_name} is going to buy the meal today !")
