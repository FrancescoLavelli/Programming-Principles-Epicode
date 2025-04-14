""" 
Write a program that ask the user a 
social network name 
and his password
the opens and write social and password in 1 line
separated from any character
Attention: everytime the file is open, 
must update and add the info 
not override those
"""

# social = input("What is your favorite social media? ").strip()
# password = input(
#     "and what about your password? I will safely retain it for you. No worries. ").strip()

# with open("social_list.txt", "a", encoding="utf-8") as file:
#     file.write(f"{social}&{password}\n")

"""Modify the app
add reading mode
at the beginning ask the user if he wants to read the list of socials 
or to add a new one
if add is asame as before
if read open the file in read mode
and print all the lines
prefix with - """


def add_password():
    social = input("What social do you want ot add? ").strip()
    password = input(
        "and what about your password? I will safely retain it for you. No worries. ").strip()
    with open("social_list.txt", "a", encoding="utf-8") as file:
        file.write(f"{social}&{password}\n")


def read_password():
    try:
        with open("social_list.txt", "r", encoding="utf-8") as file:
            content = file.readlines()
        for line in content:
            print("🔑", line.strip())  # to eliminate nextline character
    except FileNotFoundError:
        print(
            "The social_list.txt file doesn't exist yet. Try adding some passwords first.")


access = input(
    "do you want to read your social keys or add a new one? (digit: 'add', 'read')").strip().lower()
if access == "add":
    add_password()
elif access == "read":
    read_password()
else:
    print("Invalid option. Please enter either 'add' or 'read'.")
