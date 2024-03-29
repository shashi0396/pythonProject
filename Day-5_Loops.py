fruits = ['apple', 'banana', "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)
print(fruits)

# range function
# consider upto 10 only, initial -1
for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
    print(total)   # prints from 1 upto 5050
print(total)  # prints the total by adding 1 iteratively upto 5050
