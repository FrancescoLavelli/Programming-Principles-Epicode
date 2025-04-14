"""car1 = {
    "brand": "Fiat",
    "model": "Coupe",
    "max_speed": 200.0,
    "year": 2020,
    "is_electric": True,
}
car2 = {
    "brand": "Ferrari",
    "model": "F40",
    "max_speed": 300.0,
    "year": 2010,
    "is_electric": False,
}


def drive_fast(car_brand, car_model, car_speed):
    print(f"The {car_brand} {car_model} is speeding at {car_speed} km/h!")


drive_fast(car1["brand"], car1["model"], car1["max_speed"])
drive_fast(car2["brand"], car2["model"], car2["max_speed"])
"""
"""***CLASSES***"""


class Car:  # Classes you use PascalCase
    def __init__(self, brand, max_speed, year, is_electric, weight):
        # print(self)
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        self.is_electric = is_electric
        self.weight = weight

    # the method must always have at least 1 parameter -> self)
    def drive_fast(self, destination):
        # destination is not an istance parameter but an external so we need to pass it when calling the function
        print(
            f"The {self.brand} is speeding at {self.max_speed} km/h to {destination}!")


car1 = Car("Fiat", 200.0, 2020, True, 1500)
car2 = Car("Ferrari", 300.0, 2010, False, 1300)


# with the class I created my methods and I can access those. I LOVE THAT!!!
# with classes we create our datatype
# reminder a method is a function stricltly connected to an object
# init method is automatically called when we are going to create a new class objetct, like below we do not need to add __init__() at the end
# I utilize self so i can add parameters to every new class object. Self is given value in automatic and its value is the object we going to create.
# I can demonstrate it printing self inside the class to see that is == to printing the object we have created result = <__main__.Car object at 0x104699a90> (for both)
"""
    self.parameter = attribute
"""

print(car1.brand)
print(f"The {car2.brand}, max speed is: {car2.max_speed}")
print(car1)

car1.drive_fast("Genoa")

# I can add some instance attribute later      istance synonim of object

car1.doors = 5
print(car1.doors)
print(car2.doors)

del car1.doors  # to delete the instance attribute
