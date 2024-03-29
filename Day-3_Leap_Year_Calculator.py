# leap year calculation
# year should be evenly divisible by 4 , with no reminder
# not evenly divisible by 100 , left with reminder
# the year also divisible by 400, with no reminder

year = int(input("Please enter a year:\n "))
if year % 4 == 0 and year % 100 != 0:
    print("It is a leap year")
elif year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# or

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("leap year")
# else:
#     print("Not leap year")