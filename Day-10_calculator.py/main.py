from art import logo
from replit import clear


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} ot type 'n'to exit") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()

# Print vs return

# answer = calculation_function(calculation_function(num1, num2), num3)

# Through 'return' we are able to take the result from that calculation function and plug it right back into 
# another calculation function using the result of that function call as the input to another function call.
# only able to do this because I'm using the return statement and because I have outputs from my functions.

# answer = calculation_function(calculation_function(num1, num2), num3)

# print(f"{num1} {operation_symbol} {num2} = {answer}")

# Recursion

# a function that calls itself is called as recursion
# but should be careful there should be some exit function otherwise it will end itself in infinite loop

# for e.g:
# def something():
#     print("aaaaaa")

# something()
