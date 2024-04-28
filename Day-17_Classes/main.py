class User:  # class keyword , name - name of the class, should be in 'Pascal' class

    def __init__(self, user_id, username):
        print("new user being created")

        # everytime , when we create a new user under class User
        # this print statement will be triggered

        self.id = user_id
        self.username = username
        self.followers = 0  # in case we want to have 'DEFAULT' values, there is no need to pass parameters here
        self.following = 0

        # as per naming convention , name of the parameter ie, (username) = name of attribute ie, (username)
        # but don't always have to stick to these rules

    # adding method to a class
    def follow(self,user):  # unlike a function, 'method' always needs to have a 'self' parameter as the first parameter.
        # This means that when this method is called, it knows the object that called it.
        user.followers += 1
        self.following += 1


user_1 = User("001","angela")  # indent expected error, if we want to leave the class empty , use 'pass' in the function
user_2 = User("002", "jack")

user_1.follow(user_2)   # calling the method
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# cases
# PascalCase
# camelCase : first word is lower, except same as pascal case
# snake_case : all lower case and separated by underscore.

###### """"adding attributes to the class""""""  ############
# attribute is variable that is associated with an object
# user_1.id = "001"
# user_1.username = "shashi"

print(user_1.username)
print(user_1.id)
print(user_1.followers)


# user_2 = User()  # __init__ function will be triggered here after user 1, when we call 'Class'
# user_2.id = "002"
# user_2.username = "jack"


# Constructor
# part of the blueprint which specifies, what should happen when our object is being constructed
# this is also known as 'initializing an object'
# def __init__(self) # initialize attributes
# 'init' function must be called everytime you create a 'new object' from this class


# how do we set the attributes in the constructor
class Car:
    def __init__(self, seats):  # ('self' is the actual object that's being created or initialized,
        # in addition, you can as many parameters as you wish,
        # that parameter is going to be passed in when an object gets constructed from this class
        self.seats = seats

    # adding a 'method' to a class
    def enter_race_mode(self):
        self.seats = 5


my_car.enter_race_mode()  # object.method
