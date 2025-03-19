import random


bot_name = "\u2660\u2660\u2660TheJoker\u2660\u2660\u2660"  # ♠"


def guessing_game():

    random_number = random.randint(1, 100)

    while True:
        print(f"Hi, I am {bot_name}, do you wanna play with me?")
        print("1. Yes")
        print("2. No")

        choice = input(f"{bot_name}: Enter your choice (1-2): ")

        if choice == "1":
            print(f"{bot_name}: Okay, I'm thinking of a number between 1 and 100.")
            guess = None
            attempts = 0

            while guess != random_number:
                try:
                    guess = int(input(f"{bot_name}: Take a guess: "))
                    attempts += 1

                    if attempts == 5:
                        print(f"{bot_name}: I won. You didn't guess it!")
                        break
                    elif guess < 1 or guess > 100:
                        print(
                            f"{bot_name}: The number must be between 1 and 100.")
                    elif guess < random_number:
                        print(f"{bot_name}: Too low!")
                    elif guess > random_number:
                        print(f"{bot_name}: Too high!")
                    else:
                        print(
                            f"{bot_name}: Congratulations! You guessed the number in {attempts} attempts.")
                        break

                except ValueError:
                    print(f"{bot_name}:Invalid input. Please enter a number.")
        elif choice == "2":
            print(f"{bot_name}:Exiting program...")
            break

        else:
            print(f"{bot_name}:Invalid choice. Please enter 1, or 2.")


if __name__ == "__main__":
    guessing_game()
