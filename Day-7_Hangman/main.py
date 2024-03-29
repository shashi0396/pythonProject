# hangman

import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages

# CH_1: Picking a Random words and checking answers
# CH_2: Replacing blanks with guesses
# CH_3: Checking if the player has won or not
# CH_4: Keeping track of the player's lives
# CH_5: Improving the user experience

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_length = random.choice(word_list)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"


end_of_game = False
lives = 6

print(logo)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess},that's not in the word.You lose a life")
        if lives == 0:
            end_of_game = True
            print(f"You lost! The word was: {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
