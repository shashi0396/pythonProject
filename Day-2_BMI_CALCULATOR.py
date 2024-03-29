
weight = input("Enter your weight in kgs: ")
height = input("Enter your height in mt: ")

w = float(weight)
h = float(height)
# print(type(weight))

BMI = w/h**2

# print(round(BMI))
bmi_as_int = int(BMI)
# print(BMI)
print(bmi_as_int) # Converts the float o/p to whole number