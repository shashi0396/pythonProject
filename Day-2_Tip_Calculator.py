
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $\n"))
tip_percent = int(input("what percentage tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))
total = bill + (bill * tip_percent/100)
each_person_bill = total / people
each_person_bill = "{:.3f}".format(each_person_bill)

print(f"Each person should pay:{each_person_bill}")

