"""
    1. Define a class to represent a book
    2. Following instance attributes: title, author, publication year, price
    3. The Class has a method that is printing all its attributes
    
    4. once complete create 2 objects passing 1 argument for each instance attribute
    5. Call the method on both objetcs
    6. verify is correct and working
"""


class Book:
    def __init__(self, title, author, publication_year, price):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.price = price

    def one_method_to_print_them_all(self):
        print(f"{self.title} is a book created by the genius of {self.author} in {self.publication_year}, it can be yours for only ${self.price}, don't waste this oppurtunity it will last only until today!")


lotr = Book("Lord of The Rings", "J.R.R. Tolkien", 1954, 19.99)
ivanhoe = Book("Ivanhoe", "Sir Walter Scott", 1819, 8.99)

lotr.one_method_to_print_them_all()
ivanhoe.one_method_to_print_them_all()
