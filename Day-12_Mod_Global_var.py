# Modifying the global scope

enemies = 1


def increase_enemies():
    enemies += 1  # you can't directly call global variable under local scope, throws error
    global enemies  # you can call like this, but not recommended way
    # it's prone to creating bugs and errors. Because this variable with global scope could have been created
    # anywhere in your code,And you would be modifying it completely independent of when you created it.

    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# How can you achieve this without modifying the global scope within the function?

enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants

# Global scope can be incredibly useful especially when you're defining constants.
# Global constants are variables which you define
# So usually, in order to differentiate these constants which you're pretty much never going to change
# from the variables which you are likely to change, the naming convention in Python is to turn it into all UPPERCASE.

PI = 3.14159
URL = "https://en.wikipedia.org/wiki"
TWITTER_HANDLE = "@yu_angela"


# later on in your function and you want to use one of these global constants, as soon as you type it,
# you can see it's the uppercase and you know to remind yourself to not modify this inside your code.

def calc():
    TWITTER_HANDLE