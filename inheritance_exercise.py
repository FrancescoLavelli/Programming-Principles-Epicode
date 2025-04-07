"""Create a class Person
name
age
Create another class Movie_Director
which inherits from Person class
signature_movie attr

Instance an onject of superclass
instance an object of the subclass
and verify which attributes are accessible on these
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name_is(self):
        print(f"Hi, my name is {self.name}, I'm {self.age} old")

    def introduce_yourself(self):
        self.my_name_is()


class Movie_Director(Person):
    def __init__(self, name, age, signature_movie):
        super().__init__(name, age)
        self.signature_movie = signature_movie

    def get_signature_movie(self):
        print(f"My best movie is {self.signature_movie}")

    def introduce_yourself(self):
        self.my_name_is()
        self.get_signature_movie()


woody_allen = Person("Woody", 85)
# woody_allen.my_name_is()

woody_director = Movie_Director("Allen", 89, "Match Point")
# woody_director.get_signature_movie()

# Using the new combined method
woody_director.get_signature_movie()

print(woody_allen.name)
print(woody_allen.age)
print(woody_director.name)
print(woody_director.age)
print(woody_director.signature_movie)
# print(woody_allen.signature_movie) not accessible

print(issubclass(Person, Movie_Director))
print(issubclass(Movie_Director, Person))
print(isinstance(woody_director, Person))
print(isinstance(woody_director, Movie_Director))
print(dir(Person))
print(dir(Movie_Director))
print(Person.__dict__)
print(Movie_Director.__dict__)
print(woody_allen.__dict__)
print(woody_director.__dict__)
print(Person.__str__)
print(Movie_Director.__str__)
print(woody_allen.__str__)
print(woody_director.__str__)


woody_allen.introduce_yourself()
woody_director.introduce_yourself()
