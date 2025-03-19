"""
Age Calculator

This script calculates a person's age in years, months, and days based on their date of birth.
It provides an accurate calculation that handles leap years and different month lengths correctly.
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


def calculate_age(birth_date):
    """
    Calculate the age given a birth date.

    Args:
        birth_date (datetime): The date of birth as a datetime object

    Returns:
        tuple: A tuple containing (years, months, days) representing the age

    Raises:
        ValueError: If the birth date is in the future
    """
    # Get current date and time
    now = datetime.now()

    # Check if birth date is in the future
    if birth_date > now:
        raise ValueError("Birth date cannot be in the future")

    # Calculate the difference using dateutil for accurate calculation
    diff = relativedelta(now, birth_date)

    return diff.years, diff.months, diff.days


def get_birth_date():
    """
    Prompt the user for their date of birth and convert it to a datetime object.

    Returns:
        datetime: The user's date of birth as a datetime object

    Raises:
        ValueError: If the input format is invalid
    """
    print("***Please enter your date of birth (yyyy-mm-dd)***")

    try:
        date_str = input().strip()
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")
        return birth_date
    except ValueError:
        raise ValueError("Invalid date format. Please use yyyy-mm-dd format.")


def display_age_info(birth_date):
    """
    Display age information based on the provided birth date.

    Args:
        birth_date (datetime): The date of birth as a datetime object
    """
    # Calculate age
    years, months, days = calculate_age(birth_date)

    # Display the result
    print(f"You are {years} years, {months} months, and {days} days old")

    # Additional information about birth day
    day_of_year = birth_date.timetuple().tm_yday
    print(f"You were born on the {day_of_year}th day of the year")

    # Calculate days until next birthday
    today = datetime.now()
    next_birthday = datetime(today.year, birth_date.month, birth_date.day)

    # If birthday has already passed this year, get next year's birthday
    if next_birthday < today:
        next_birthday = datetime(
            today.year + 1, birth_date.month, birth_date.day)

    days_until_birthday = (next_birthday - today).days
    print(f"Your next birthday is in {days_until_birthday} days")


def main():
    """Main function to run the age calculator program."""
    try:
        birth_date = get_birth_date()
        display_age_info(birth_date)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
