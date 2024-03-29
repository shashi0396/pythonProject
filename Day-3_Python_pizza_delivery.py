# Automatic Pizza order program

print("Welcome to the Python Pizza Deliveries!")
size = input("What size do you want ? S , M , L\n")
bill = 0
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"you final bill: ${bill}")