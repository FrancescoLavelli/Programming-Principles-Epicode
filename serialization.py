"""Serialization
    serialize objects into byte stream
"""

"""json"""


# we need to import the module json to call the function dump who takes to argument the data we want to serialize and the destination where we want to write the data

import json
shopping_list = ["pear", "orange", "apple"]

with open("shopping_list.json", "w", encoding="utf-8")as file:
    json.dump(shopping_list, file)

# lets serialize a dictionary
shopping_list = {"pear": 5, "orange": 15,
                 # you will see that True is true and None is null in json
                 "apple": 25, "bananas": True, "nuts": None}
with open("shopping_list.json", "w", encoding="utf-8")as file:
    json.dump(shopping_list, file)

# to deserialise it and read it
with open("shopping_list.json", "r", encoding="utf-8")as file:
    read_shopping_list = json.load(file)

print(read_shopping_list)
