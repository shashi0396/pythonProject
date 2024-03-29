#     A    B    C
# 1 [" ", " ", " "]
# 2 [" ", " ", " "]
# 3 [" ", " ", " "]

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map1 = [line1, line2, line3]

print("Hiding your treasure! X marks the spot,")
position = input("Enter your position: ")
letter = position[0].lower()       # list is indexed
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
# in order to compare letters and point the position of the input , be default it starts with zero

number_index = int(position[1]) - 1  # take the input from
map1[letter_index][number_index] = "X"

print(f"{line1}\n{line2}\n{line3}")


