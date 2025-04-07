class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def process_payment(self):
        print(f"Processing payment of {self.amount} {self.currency}")

    def engage_payment(self):
        print("Authorization in progress...")
        self.process_payment()


class CreditCardPayment(Payment):
    # I need to add the parameter of the orginal superclass and give em a value, otherwise it will not work
    def __init__(self, amount, currency, card_number, expiration_date):
        # I define the parameters here, calling the one of the superclass
        super().__init__(amount, currency)
        self.card_number = card_number
        self.expiration_date = expiration_date

    def process_payment(self):
        print(
            f"Processing credit card payment of {self.amount} {self.currency} with card number {self.card_number} and expiration date {self.expiration_date}")


class PayPalPayment(Payment):
    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email

    def process_payment(self):
        input("Enter password: ")
        super().process_payment()


class PrimePayPalPayment(PayPalPayment):
    def __init__(self, amount, currency, email, discount):
        super().__init__(amount, currency, email)
        self.discount = discount
        self.amount *= 1 - self.discount / 100


# payment = Payment(100, "USD")
# payment.process_payment()

credit_card_payment = CreditCardPayment(
    200, "EUR", "1234567890123456", "12/25")
# credit_card_payment.process_payment()
credit_card_payment.engage_payment()

paypal_payment = PrimePayPalPayment(500, "QAR", "putu@gmail.com", 25)
# paypal_payment_1 = PrimePayPalPayment(500, "QAR", "putu@gmail.com", 25)
# paypal_payment_2 = paypal_payment
paypal_payment.engage_payment()

print(issubclass(PayPalPayment, Payment))
print(issubclass(PayPalPayment, PayPalPayment))
print(isinstance(paypal_payment, Payment))
print(isinstance(paypal_payment, PayPalPayment))
print(isinstance(paypal_payment, PrimePayPalPayment))
print(isinstance(paypal_payment, CreditCardPayment))
# print(paypal_payment is paypal_payment_1)
# print(paypal_payment_2 is paypal_payment)

"""Override
means that in a subclass I define a method with the same name of another method who is present in the superclass. 
If I do the interpeter will adopt the one of the subclass. Who has the priority. The interpeter control the methods from the subclass to the class. I can just use the super().method() again to override the one of the mainClass and call it """

"""Multi-Level Inheritance
you can nest super() in various classes to call methods in the upper classes set as parameters: class PrimePayPalPayment(PayPalPayment)

issubclass() tells us if A is sublcass of B 
isinstance() takes and object and a class as parameters and tells who ineherits what from who
is I can ask about 2 object
"""

"""Polymorphism
A same element(like the method process_payment() in this page) can have multiple forms, depends on where is called
"""

"""Composition
It is an alternative to inheritance
"""
