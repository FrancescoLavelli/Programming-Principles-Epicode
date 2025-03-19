"""Lesson#3
"""

GRAVITY = 9.81
PI = 3.14
print(PI)
PI = 2
print(PI)

# Bynary numbers: you need to ad the prefix 0b
print(0b01010101010101010)
# Octal Numbers: 0o
print(0o1213444)
# Hexadecimal: 0x
print(0x123434fff)

# elevare a potenza
power_of = print(15e9)
print(type(power_of))

print(type(GRAVITY))


# methods
title = "   \t il signore degli anelli \n\n    "
# third argument is for how many occorrencies we want to substitute the first with the second argument
title2 = title.strip().replace("signore", "Dominatore", 1)
print(title2)

# .strip()  # strip spaces beginning and end
# .replace()  # sostituisce una sottostringa in una stringa
