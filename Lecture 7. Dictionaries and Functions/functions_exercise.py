"""_summary_
Define 2 dictionaries
keys: name, + others
Both dict must have a key: age 
which is = to none as start

DEFINE A FUNCTION WHO TAKES birth year as user input
calculate the age and return it
in the input message we have to print user name 
so we need to pass it to the function as argument

to calculate age we need actual year
that needs to be passed in the function
call the function twice
one for each dictionary
"""
from datetime import datetime

# Create a datetime object
now = datetime.now()

# Get the time tuple
time_tuple = now.timetuple()

user1 = {
    "name": "John",
    "age": None,
    "profession": "Dentist",
    "Car": "Challenger SR8",
}

user2 = {
    "name": "Michael",
    "age": None,
    "profession": "Web Dev",
    "Car": "Mustang GT",
}


def age_calculator(username, birth_year):
    age = time_tuple.tm_year - birth_year
    print(f"{username} is {age} years old")
    return age


age_calculator("John", 2007)
age_calculator("Michael", 1985)


"""Prof Solution"""


def calculate_age(name, current_year):
    birth_year = int(input(f"{name}, please insert birthyear: "))
    return current_year - birth_year


user1["age"] = calculate_age(user1["name"], 2025)
user2["age"] = calculate_age(user2["name"], 2025)

print(user1, user2)
