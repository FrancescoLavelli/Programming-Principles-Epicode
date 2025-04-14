
curr_year = 2025
birth_year = int(input("Insert you year: "))

age = curr_year - birth_year
if age >= 18:
    is_adult = True
    print("You are an adult")
else:
    is_adult = False
    print("Stand off Kiddo")
print(f"You are {age} years old")
print(is_adult)
