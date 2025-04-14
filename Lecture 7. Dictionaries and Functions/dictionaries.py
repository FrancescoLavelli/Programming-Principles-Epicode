
"""** TO VALUES WE CAN ASSIGN ANY TYPE OF VALUES TO THE KEYS WE CAN ASSIGN ONLY IMMUTABLE TYPES("STR", INT)"""

car = {
    "color": "red",
    "price": 35_000.,
    "year": 2024,
    "is_hybrid": True,
}

car["price"] = 25_000.  # I can Modify
car["weight"] = 1500  # I can add

# with get method I can put a second argument to return a value (instead of none if the key is not present in the dict)
print(car.get("model", 0))

for el in car:
    print(el)

print(car.keys())
print(car.values())
print(car.items())

for key, val in car.items():
    print(key, val)

car.pop("color")
car.popitem()  # di default remove the last key

print(car)
