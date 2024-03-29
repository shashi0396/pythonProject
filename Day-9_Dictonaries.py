programming_dictionary = {
    "Bug": "An error in the program, that prevents the program from running as expected",
    "function": "I also know what you are doing."
}

# Adding new items to dictionary

programming_dictionary["Loop"] = " The action of doing something over and over again"

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# specifying which is key and which is value in the dictionary to the program
name = input("What is your name?: ")
price = int(input("What is your bid?: $"))
# for.eg bids is dictionary, bids{}
bids[name] = price  # telling the python that 'name' is 'key' and 'price' is 'value'


# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    # only gave the keys
    print(programming_dictionary[key])
    # loop through the values if passed like this

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille","Dijon"],
    "Germany": ["Berlin", "Hamburg","Stuttgart"]
}

# nest a list in a list
# ["A","B",["C","D"]]

# Nesting a dictionary in a dictionary
travel_logs = {
    "France": {"cities_visited":["Paris", "Lille","Dijon"],
               "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg","Stuttgart"],
                "total_visits": 5}
}

#nest a dictionary in a list

travel_logs1 = [
    {
    "country":"France",
    "cities_visited":["Paris", "Lille","Dijon"],
    "total_visits": 12
},
{
    "country":"Germany",
    "cities_visited": ["Berlin", "Hamburg","Stuttgart"],
    "total_visits": 5
    }
]

# example: print 'steak' from the dictionary

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])



