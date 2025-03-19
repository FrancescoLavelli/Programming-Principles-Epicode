import itertools

# 1. Classic while True loop


def classic_infinite():
    while True:
        user_input = input("Enter 'q' to quit: ")
        if user_input == 'q':
            break
        print("Looping...")

# 2. Using a flag variable


def flag_based():
    run = True
    while run:
        user_input = input("Enter 'q' to quit: ")
        if user_input == 'q':
            run = False
        else:
            print("Still looping...")

# 3. Using itertools.cycle


def itertools_infinite():
    for _ in itertools.cycle([0]):
        user_input = input("Enter 'q' to quit: ")
        if user_input == 'q':
            break
        print("Cycling...")

# 4. Using recursion (with safety limit)


def recursive_loop(count=0):
    if count >= 5:  # Safety to prevent stack overflow
        return
    user_input = input("Enter 'q' to quit: ")
    if user_input != 'q':
        print(f"Recursion count: {count}")
        recursive_loop(count + 1)


if __name__ == "__main__":
    print("=== Classic while True ===")
    classic_infinite()

    print("\n=== Flag-based loop ===")
    flag_based()

    print("\n=== itertools.cycle ===")
    itertools_infinite()

    print("\n=== Recursive loop (5 max) ===")
    recursive_loop()
