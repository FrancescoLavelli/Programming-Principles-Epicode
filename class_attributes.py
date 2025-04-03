class Car:
    wheels = 4  # class attribute = for everyone
    total_built_car = 0
    __total_driven_km = 0

    def __init__(self, brand, max_speed, year, is_electric, weight):
        # print(self)
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        self.is_electric = is_electric
        self.weight = weight
        # we are certain that this code line will be called everytime the method is called, so everytime an object car is created
        Car.total_built_car += 1

    def drive(self, kilometers):
        print(f"{self.brand} is driving for {kilometers}")
        Car.__total_driven_km += kilometers

    def __str__(self):
        return f"I am an amazing {self.brand} from {self.year}"


car1 = Car("Fiat", 200.0, 2020, True, 1500)
car2 = Car("Ferrari", 300.0, 2010, False, 1300)

print(Car.wheels)
print(Car.total_built_car)

car1.drive(15)
car2.drive(30)
car1.drive(40)
car2.drive(50)

# I could manually reset the attribute. but Car.total_driven_km is unchanged
car1.total_driven_km = 0

print(Car.total_driven_km)

""" *********INTROSPECTION********* """
# THIS METHOD ALLOW US TO INSPECT THE OBJECT DURING RUNTIME
print(type(car1))
print(dir(car1))
print(dir(Car))
# cosi facendo vedo tutti gli elementi dello scope in questo punto accessibili
print(dir())
# restituisce un boolean (obj, "attr") or (obj, "method")
print(hasattr(car1, "brand"))
# return a dictionary with instance attribute, __dict__ is an attribute
print(car1.__dict__)
# return in which script python the object or class is being created module = script
print(car1.__module__)
print(car1.__str__())

""" *********REFLECTION*********"""
# reflection allow us to analyse and modify the objects "dinamically during runtime"
new_attr = input("How do you want to call the new attribute?")
setattr(car1, new_attr, 1500)
print(car1.weight)

# with setattr can I add new attributes or modify existing ones
mod_attr = input("What is the name of the attribute you want to modify?")
new_val = input("What is the new value?")
setattr(car1, mod_attr, new_val)
print(car1.brand)

# is giving back the value of the attribute we want to check
getattr(car1, "brand")

# attribute protection: I need to make it private, to do so I need to name it with __ DOUBLE UNDERSCORE Dunder method
# this way the methods cannot be called from outside the class

# I am creating a new instance attribute which will have the given value but It wont override the private class one (with the same name)
car1.__total_driven_km = 0
