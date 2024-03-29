weight = input("Enter your weight in kgs: ")
height = input("Enter your height in mt: ")

w = float(weight)
h = float(height)
# print(type(weight))

BMI = round((w / h ** 2), 2)

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal weight")
elif BMI < 30:
    print("You are slightly overweight")
elif BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")
