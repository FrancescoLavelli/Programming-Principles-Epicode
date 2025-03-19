"""**Celsius FARENHEIT CONVERTER"""

# VERSION 1.0
# print("Insert the Celsius to be converted: ")
# celsius = float(input())
# fahrenheit = celsius * 9 / 5 + 32
# print(f"{celsius} Celsius are equal to {fahrenheit} Fahrenheit")

# VERSION 2.0


def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)


def get_temperature(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            celsius = get_temperature("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == '2':
            fahrenheit = get_temperature("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
