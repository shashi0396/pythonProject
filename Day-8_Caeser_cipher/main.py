from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# CH:2
# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}")


print(logo)
should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' ?\n")

    if restart.lower() == "no":
        should_end = True
        print("GoodBye...!")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for char in plain_text:
#         position = alphabet.index(char)
#         new_position = (position + shift_amount) % len(alphabet)
#         new_char = alphabet[new_position]
#         cipher_text += new_char
#     print(f"The Encoded cipher text is: {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = (position - shift_amount) % len(alphabet)
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The Decrypted cipher text is : {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Invalid input direction")
