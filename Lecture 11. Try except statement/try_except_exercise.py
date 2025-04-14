"""
    define a list with 3 tourisic destinations
    print them all
    ask user where does he want to go
    to select he has to insert the index number 0 1 2
    print have a safe travel + destination_chosen


try to break the app to find exceptions
handle the exceptions with a try block
TIP: you should find 2 main exceptions

Add Raise Error for numbers <= 0

Bonus:
Move out of the TRY block all critical commands 
and move it in a different branch that will execute only if no exception is raised

Give to negative number a specific exceptionCreate a custom one with personalised message
raise it
wsap with the previous one
Handle this exception with a except branch
"""


class NegativeNumberError(Exception):

    def __init__(self, message):
        super().__init__(message)


destinations = ["Rio", "Bora Bora", "Tonga"]

# Print destinations with their index numbers (starting from 1)
print("Available destinations:")
for index, destination in enumerate(destinations, start=1):
    print(f"{index}: {destination}")

# Get user input for destination index
final_destination_index = input(
    "Enter the index number of where you want to go (1-3): ")

try:
    # Convert input to integer
    index = int(final_destination_index)

    # Convert from 1-based index to 0-based index for list access
    chosen_destination = destinations[index-1]
    # raise and error
    if index <= 0:
        # raise Exception("Number must be greater than 0")
        # raise NegativeNumberError("Number must be greater than 0")#custom class option 1
        raise NegativeNumberError()

     # This will raise IndexError if index is out of range


except NegativeNumberError:
    print("Error: Please enter a number greater than 0")
except IndexError:
    print("Sorry, the destination selected is not present.",
          f"Please select a number between 1 and {len(destinations)}")
except ValueError:
    print("Error: Please enter a valid number")
except Exception as e:
    print(f"Error: {e}")
else:
    print("The program has been executed successfully")
    print(f"Have a safe travel to {chosen_destination}")
finally:
    print("Thank you for using our travel service!")
