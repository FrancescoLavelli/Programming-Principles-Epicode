panda = {
    "color": "red",
    "price": 35_000.,
    "year": 2024,
    "is_hybrid": True,
}

punto = {
    "color": "red",
    "price": 25_000.,
    "year": 2014,
    "is_hybrid": False,
}

# discount_price = panda["price"] * 0.7
# if discount_price > 20_000:
#     discount_price -= 100
# print(discount_price)
# if we want to apply the same discount to punto we have to duplicate the code, so we use functions instead


def discount_price(price):
    discount_price = price * 0.7
    if discount_price > 20_000:
        discount_price -= 100
    return


disc_price = discount_price(panda["price"])
print(disc_price)
discount_price(punto["price"])

""" Optional Parameters"""


# selecting the default value we make the parameter optional
def discount_price(price, bonus_discount=100):
    discount_price = price * 0.7
    if discount_price > 20_000:
        discount_price -= bonus_discount
    return


""" Arbitrary Numbers of Parameters"""


# adding * let the parameter became a list = *args
def discount_price(price, *bonus_discount):
    discount_price = price * 0.7
    if discount_price > 20_000:  # adding **kwargs I'm adding an arbitrary number of keyword arguments
        for discount in bonus_discount:
            discount_price -= discount
    return discount_price


discounts = [100, 150, 200, 250, 300, 1000]
disc_price = discount_price(panda["price"], *discounts)
print(disc_price)


""" Recursive function"""

# def say_hello():
#     print("Hello")
#     say_hello()

# say_hello()


def factorial(n):
    print("-", n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 4! = 4x3x2x1
# 1! = 1
# 0! = 1


print(factorial(4))
