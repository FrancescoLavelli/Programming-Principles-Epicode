var = 9
guess = int(input("number: "))

if guess == var:
    print("Bravo")
elif guess in range(0, 10):
    print("Epic fail")
else:
    print("the number must be 0-9")
