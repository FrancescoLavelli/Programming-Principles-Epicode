""" **Age Calculator**
    
    The assignment:
    1. **Ask for user DOB
    2. **Use DOB to calculate user_age
    3. **Print user_age
    
This script calculates a person's exact age in years, months, and days
based on their date of birth and the current date.
"""


from datetime import datetime, date, time
import calendar
import sys

""" **Working with date and time**
# Current date and time
now = datetime.now()  # 2023-03-12 17:17:07.415875

# Creating specific dates and times
specific_date = datetime(2023, 3, 12, 17, 17, 7)

# Just date or just time
today = date.today()  # 2023-03-12
current_time = time(17, 17, 7)  # 17:17:07

# Difference between dates
tomorrow = today + timedelta(days=1)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # "2023-03-12 17:17:07"

# Parsing
parsed = datetime.strptime("2023-03-12 17:17:07", "%Y-%m-%d %H:%M:%S")"""

""" **Solution #1**
    The Barbarian Way
"""

# print("***Please Insert your date of birth: yyyy-mm-dd***")
# birth_date = datetime.strptime(input(), "%Y-%m-%d")
# today = datetime.today()
# if today.month < birth_date.month:
#     age = (today.year - birth_date.year) - 1
# else:
#     age = today.year - date_of_birth.year

# print("\*" * 43)
# print(f"***You are {age} years old***")
# print("\*" * 43)
# find a way to get the date from another object. Find out which one includes all the data.

""" **Solution #2**
    Refine if you can
"""
# # Create a datetime object
# now = datetime.now()

# # Get the time tuple
# now_tuple = now.timetuple()

# # Get user date of birth
# print("***Please Insert your date of birth: yyyy-mm-dd***")
# # Transform the str in datetime plus input validation
# try:
#     date_str = input().strip()
#     birth_date = datetime.strptime(date_str, "%Y-%m-%d")

# except ValueError:
#     raise ValueError("Invalid date format. Please use yyyy-mm-dd format.")

# # Get the time tuple for the user birth_date
# birth_tuple = birth_date.timetuple()

# # Doing the Maths
# years = now_tuple.tm_year - birth_tuple.tm_year
# # Adjust years if the birthday hasn't occurred yet this year
# if (now_tuple.tm_mon, now_tuple.tm_mday) < (birth_tuple.tm_mon, birth_tuple.tm_mday):
#     years -= 1

# months = now_tuple.tm_mon - birth_tuple.tm_mon
# # Adjust months if the day of month hasn't occurred yet this month
# if now_tuple.tm_mday < birth_tuple.tm_mday:
#     months -= 1
#     if months < 0:
#         months += 12

# days = now_tuple.tm_mday - birth_tuple.tm_mday
# # Adjust days if the day of month hasn't occurred yet this month
# if days < 0:
#     # Get the number of days in the previous month
#     if now.month == 1:
#         previous_month = 12
#         previous_month_year = now.year - 1
#     else:
#         previous_month = now.month - 1
#         previous_month_year = now.year

#     days_in_previous_months = calendar.monthrange(
#         previous_month_year, previous_month)[1]
#     days += days_in_previous_months

# print(f"You are {years} years, {months} months and {days} days old")

# # born in this day of the year (always running)
# print(f"You are born on the {birth_tuple.tm_yday} day of the year")

""" **Solution #3**
    Adding functions and finesse
"""


def get_birth_date():
    """
    Get the user's birth date from input with validation.

    Returns:
        datetime: A datetime object representing the user's birth date.

    Raises:
        ValueError: If the input date format is invalid.
        SystemExit: If user provides invalid input after multiple attempts.
    """
    print("***Please Insert your date of birth: yyyy-mm-dd***")

    # Allow up to 3 attempts for valid input
    for attempt in range(3):
        try:
            date_str = input().strip()
            birth_date = datetime.strptime(date_str, "%Y-%m-%d")

            # Ensure birth date is not in the future
            if birth_date > datetime.now():
                print("Error: Birth date cannot be in the future. Please try again.")
                continue

            return birth_date

        except ValueError:
            if attempt < 2:  # Still have attempts left
                print(
                    "Invalid date format. Please use yyyy-mm-dd format (e.g., 1990-01-31).")
            else:  # Last attempt failed
                print("Too many invalid attempts. Exiting program.")
                sys.exit(1)


def calculate_age(birth_date, current_date=None):
    """
    Calculate the exact age in years, months, and days.

    Args:
        birth_date (datetime): The date of birth
        current_date (datetime, optional): 
            The reference date for age calculation.
            Defaults to current date/time.

    Returns:
        tuple: Contains (years, months, days) representing the age
    """
    # Use current date if not specified
    if current_date is None:
        current_date = datetime.now()

    # Get time tuples for easy access to components
    now_tuple = current_date.timetuple()
    birth_tuple = birth_date.timetuple()

    # Calculate years
    years = now_tuple.tm_year - birth_tuple.tm_year

    # Adjust years if the birthday hasn't occurred yet this year
    if (now_tuple.tm_mon, now_tuple.tm_mday) < (birth_tuple.tm_mon, birth_tuple.tm_mday):
        years -= 1

    # Calculate months
    months = now_tuple.tm_mon - birth_tuple.tm_mon

    # Adjust months if the day of month hasn't occurred yet this month
    if now_tuple.tm_mday < birth_tuple.tm_mday:
        months -= 1
        if months < 0:
            months += 12

    # Calculate days
    days = now_tuple.tm_mday - birth_tuple.tm_mday

    # Adjust days if the day of month hasn't occurred yet this month
    if days < 0:
        # Get the number of days in the previous month
        if current_date.month == 1:
            previous_month = 12
            previous_month_year = current_date.year - 1
        else:
            previous_month = current_date.month - 1
            previous_month_year = current_date.year

        days_in_previous_month = calendar.monthrange(
            previous_month_year, previous_month)[1]
        days += days_in_previous_month

    return years, months, days


def get_day_of_year(date):
    """
    Get the day of the year (1-366) for a given date.

    Args:
        date (datetime): The date to calculate the day of year for

    Returns:
        int: The day of the year (1-366)
    """
    return date.timetuple().tm_yday


def main():
    """
    Main function to run the age calculator program.
    """
    try:
        # Get the current date and time
        now = datetime.now()

        # Get user's birth date
        birth_date = get_birth_date()

        # Calculate age
        years, months, days = calculate_age(birth_date, now)

        # Print results
        print(f"You are {years} years, {months} months and {days} days old")
        print(
            f"You are born on the {get_day_of_year(birth_date)} day of the year")

        # KeyboardInterrupt is raised when the user presses Ctrl+C (or similar interrupt key combination) to forcibly terminate the program
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
        # sys.exit(0) terminates the program with exit code 0, indicating successful termination without errors (this is a convention)
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # sys.exit(1) terminates the program with exit code 1, indicating termination due to an error (this is a convention)
        sys.exit(1)

        # sys.exit(0)`: Indicates normal/successful termination (no errors)
        # sys.exit(1)`: Indicates abnormal termination (error occurred)


if __name__ == "__main__":
    main()
