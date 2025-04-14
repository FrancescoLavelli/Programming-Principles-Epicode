"""Transform in json
a txt file generated in the previous exercises
without altering the original
To start create and empty dict
open the file in read method
cycle through every line,
and split
to get key and value
add to the dictionary each key and value pairs
open a new file in write mode
to write the dict in it
serialise it with json.dump"""

import json

FILENAME = "social_list.txt"
password_vault = {}


def dictionarify():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            content = file.readlines()

        for line in content:
            parts = line.strip().split("&")
            if len(parts) == 2:
                social, password = parts
                password_vault[social] = password
                print("📱", social, ":", "🔑", password)

    except FileNotFoundError:
        print("The social_list.txt file doesn't exist yet.")

    else:
        # Write the dictionary to the file
        with open("password_vault_dict.txt", "w", encoding="utf-8") as file:
            for social, password in password_vault.items():
                file.write(f"{social}: {password}\n")

        print(f"Dictionary saved with {len(password_vault)} entries")


def jsonify():
    with open("password_vault_dict.json", "w", encoding="utf-8")as file:
        json.dump(password_vault, file)


def de_jsonify():
    with open("password_vault_dict.json", "r", encoding="utf-8")as file:
        read_json_file = json.load(file)
    print(read_json_file)


dictionarify()
jsonify()
de_jsonify()
