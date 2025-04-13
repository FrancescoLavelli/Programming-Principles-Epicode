# try:
#     birth_year = int(input("Insert your birth year: "))
#     age = 2025 - birth_year
#     print(f"You are {age} years old")
# except ValueError:
#     print("Error: Please insert a valid number")


# when int cannot turn string in int raise an exception

class NegativeMonthsError(Exception):
    def __init__(self, message):
        super().__init__(message)


car_price = 20_000
try:
    months = int(input("Insert the number of months: "))
    if months <= 0:
        # raise Exception("Months must be greater than 0") #using default exception
        raise NegativeMonthsError("Months must be greater than 0")
    # assert months > 0
    monthly_payment = car_price / months
except ValueError:
    print("Error: Please insert a valid number")
except ZeroDivisionError:
    print("Error: Please insert a number greater than 0")
except Exception as e:
    print(f"Error: {e}")
else:
    # print("The program has been executed successfully")
    print(f"The monthly payment is {monthly_payment}")
finally:
    # it always run. Usually used to close files/database/api. To release resources
    # print("The program has been executed successfully")
    print("The program has been executed successfully")


# I can raise errors with the keyword assert. To avoid conceptual-like errors. In this case negative numbers. si usa in fase di debugging and testing.
# for specific expeptions we can use the keyword raise

# we can instance our custom Error classes, they must finish with Error
