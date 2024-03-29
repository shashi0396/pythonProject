import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have in your password?\n"))
nr_numbers = int(input("How many numbers would you like to have in your password?\n"))

# easy way

# password = ""
#
# for char in range(0, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(f"Your password is: {password}")

# hard level
# random choice no structure

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")



