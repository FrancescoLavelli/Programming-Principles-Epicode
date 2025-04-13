class Payment:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def process(self):
        self.payment_service.make_payment()


class CreditCardPayment:
    def make_payment(self):
        print("Paying via CC")


class PayPalPayment:
    def make_payment(self):
        print("Paying via PayPal")


cc_service = CreditCardPayment()
paypal_service = PayPalPayment()

payment = Payment(cc_service)
payment.process()
