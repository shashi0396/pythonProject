height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the coaster")
    age = int(input("What is your age ?"))
    if age < 12:
        bill += 5
        print("Child tickets are $5")
    elif age < 18:
        bill += 7
        print("Youth tickets are $7")
    elif 45 <= age <= 55:
        print("Have a free ride , it's on us $")
    else:
        bill += 12
        print("Adult tickets are $12")

    with_photo = input("Do you photos while riding the coaster?(y/n")
    if with_photo == "y":
        # Add $3 to their bill
        bill += 3

    print(f"your total bill is ${bill}")

else:
    print("Sorry,you have to grow taller before can ride the coaster")
