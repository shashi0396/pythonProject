# print("use chose": rock)
# print(f"computer chose {computer_choice})

# rules for rock paper scissors
# rock wins against scissors r>s 0>2
# scissors win against paper s>p 2>1
# paper wins against rock p>r 1>0
# 0 = rock
# 1 = paper
# 2 = scissors
import random

rock = """"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]  # list indexing utilized in conditions to print image
user_choice = int(input("What do you choose? Type 0 Rock, 1 for Paper or 2 for Scissors: "))
# input is always a string, but it has to converted to int.
print("You chose")
if user_choice >= 3 or user_choice < 0:
    print("You typed a invalid number")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("YOW WON...!")
    elif computer_choice == 0 and user_choice == 2:
        print("you Lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    elif user_choice == computer_choice:
        print("Its a Draw")
