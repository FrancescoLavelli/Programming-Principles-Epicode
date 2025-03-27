"""
1.Add a new method to the book Class
    to apply a discount
    
2.The method must have a parameter
to represent the %discount
we have to apply on the original price
(which is the instance attribute price)

3.After calling the method
check in the discount hhave been applied 
check the original price is still unmodified

discounted_price = price * (100 - discount) / 100
"""


class Book:
    def __init__(self, title, author, publication_year, price, discounted_price=0):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.price = price
        self.discounted_price = discounted_price

    def one_method_to_print_them_all(self):
        print(f"{self.title} is a book created by the genius of {self.author} in {self.publication_year}, it can be yours for only ${self.price}, don't waste this oppurtunity it will last only until today!")

    def apply_discount(self, discount):
        self.discounted_price = self.price * (100 - discount) / 100
        print(f"Discounted Price: ${self.discounted_price}")
        print(f"Original Price: ${self.price}")


lotr = Book("Lord of The Rings", "J.R.R. Tolkien", 1954, 19.99)
ivanhoe = Book("Ivanhoe", "Sir Walter Scott", 1819, 8.99)

lotr.one_method_to_print_them_all()
ivanhoe.one_method_to_print_them_all()

lotr.apply_discount(30)
ivanhoe.apply_discount(70)
