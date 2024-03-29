# fizzbuzz game

# program should print each number from 1to 100 in turn and include number 100

# when the number is divisible by 3 then instead of printing the
# number , it should print "Fizz"

# when the number is divisible by 5, then instead of printing the number ,
# it should print "Buzz".

# and if the number is divisible by both 3 & 5, then instead of printing the number ,
# it should print ""FizzBuzz"

target = 50

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif number % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif number % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(number)

# Print the counts
print(f"Number of Fizz: {fizz_count}")
print(f"Number of Buzz: {buzz_count}")
print(f"Number of FizzBuzz: {fizzbuzz_count}")