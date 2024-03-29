country = input()
visits = int(input("Enter the number visits"))
lis_of_cites = eval((input("Enter the cities visited")))

travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5
    }
]


def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# TODO: Write the function that will allow new countries
# to be added to the travel_log.
# programming_dictionary["Loop"] = " The action of doing something over and over again"


add_new_country(country, visits, lis_of_cites)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
