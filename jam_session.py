"""
define a class that represents a musical instrument
Assign at least 2 instance attributes to the class
and 2 Class attributes

Instance a class object and apply Introspection:
hasattr, getattr, setattr, dir, type, __dict__, __module__, __str__
verify which attribute are accessible on the object and which are not
and which are on the class

add a method to the class that prints a message __str__

Add a private instance attribute to the class
Verify that is not accessible
Add to class definition a method that allow to access the private attribute

Add a new class method
T allow to change the private attribute value

"""


class Guitar:
    # class attributes
    strings = 6
    bridge = "wood"
    __instrument_type = "string"

    # instance attribute
    def __init__(self, brand, model, color, is_acoustic, is_electric, body=None, neck=None, pickups=None, fretboard=None, ):
        self.brand = brand
        self.model = model
        self.color = color
        self.is_acoustic = is_acoustic
        self.is_electric = is_electric
        self.body = body
        self.neck = neck
        self.pickups = pickups
        self.fretboard = fretboard

    def __str__(self):
        return f"You are playing a {self.brand} {self.model} {self.color} guitar"

    def get__instrument_type(self):
        return self.__instrument_type

    def modify_private_attribute(self, new_value):
        self.__instrument_type = new_value


fender_stratocaster = Guitar("Fender", "Stratocaster", "Sunburst",
                             False, True, "Maple", "Maple", "Single Coil", "Rosewood")
gibson_les_paul = Guitar("Gibson", "Les Paul", "Natural",
                         True, False, "Mahogany", "Maple", None, "Ebony")


print(fender_stratocaster.__dict__)
# print(gibson_les_paul.__dict__)
print(dir())
print(dir(fender_stratocaster))
# print(dir(gibson_les_paul))
print(dir(Guitar))
print(dir(fender_stratocaster.__dict__))


print(hasattr(fender_stratocaster, "strings"))
print(hasattr(fender_stratocaster, "neck"))
print(hasattr(fender_stratocaster, "price"))
print(fender_stratocaster)

# print(Guitar.__instrument_type)  # is working, attribute error
# fender_stratocaster.__instrument_type = "Drums"
# print(fender_stratocaster.__instrument_type)
# print(gibson_les_paul.__dict__)
# Guitar.__instrument_type = "Strings"
# print(Guitar.__instrument_type)
# print(fender_stratocaster.__instrument_type)
# print(Guitar.fender_stratocaster.__instrument_type) #attribute error
# print(Guitar.__instrument_type)

gibson_les_paul.modify_private_attribute("Keys")

# yes _Guitar__instrument_type: Keys
print(gibson_les_paul.get__instrument_type())
print(fender_stratocaster.get__instrument_type())  # still "string"
