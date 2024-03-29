# to work out the love score b/w 2 people:
# 1. take both people's names and check for the number of time the letters in the word TRUE occurs.
# 2. Then check for the number of time the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number

# for love scores <10 and >90 , the msg should be:
#  "your score is "x", you go together like coke and mentos
# for love scores b/w 40 and 50 , the message should be:
# your score is "y", you are alright together
# otherwise, the message will just be their score:
# your score is "z"

print("Welcome to the Love Calculator!")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_name = name1 + name2
lower_name = combined_name.lower()  # to check, whether the casing is same or not, user may use capitalized letters
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score},you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score},you are alright together")
else:
    print(f"Your score is {score}")
