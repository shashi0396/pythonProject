target = int(input("Enter a number b/w 1 and 1000:\n"))

for even_number in range(2, target+1, 2):
    target += even_number
    print(even_number)
print(target)
