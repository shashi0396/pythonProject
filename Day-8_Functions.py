# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()


# Function that allows the input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name()  # 'function' with 'parameter'-cannot be called without an 'argument'
# greet_with_name("Angela")
# greet_with_name("Billie")


# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# greet_with("Jack Bauer", "Nowhere")

# greet_with("Nowhere", "jack Bauer")
# #  this is called positional argument-- default way

# functions with keyword arguments --custom way

greet_with(location="London", name="Angela")
