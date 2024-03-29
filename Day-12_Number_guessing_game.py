from random import randint
from art import logo

EASY_LEVEL_TURNS = 10  # global_constants
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer against the guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"Congratulations! You got it! The answer was {answer}")


def set_difficulty():
    level = input("choose a difficulty.Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(" You've run out of guesses, you lose")
            return  # inorder to exit the while loop in the function
        elif guess != answer:
            print("Guess again")


game()
