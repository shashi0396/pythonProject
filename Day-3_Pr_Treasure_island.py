print('''
********************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
********************************************************************
''')
print("Welcome to the Treasure Island")
print("Your Mission is to find the treasure")
stage1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
lower_stage1 = stage1.lower()

if lower_stage1 == "left":
    stage2 = input("Would you like to 'Swim' or 'Wait for the boat'? Type 'swim' or 'wait'\n")
    lower_stage2 = stage2.lower()
    if lower_stage2 == "wait":
        stage3 = input("Which door would you like to choose? Type 'blue' or 'red' or 'yellow'\n")
        lower_stage3 = stage3.lower()
        if lower_stage3 == "red" or lower_stage3 == "blue":
            print("Game over...!")
        else:
            print("You Win....Congratulations!")
    else:
        print("Game over..!")
else:
    print("Game over..!")
