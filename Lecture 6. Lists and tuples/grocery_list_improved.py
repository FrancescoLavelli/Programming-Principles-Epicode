""" **Improved Grocery List
- Uses consistent casing for all items
- Simplified list management
- Better user prompts
- Cleaner output formatting
"""

grocery_list = [item.strip().lower() for item in ["carrot", " broccoli", "fennel", "bread",
                "hummus", "fish", "mince", "Bananas", "blueberries"]]


def list_organizer():
    grocery_list.sort()
    print("\nCurrent list:")
    for item in grocery_list:
        print(f"- {item.capitalize()}")

    while True:
        print("\nWhat do you want to buy today?\nTo Exit press: \"Q\" \n$$$:", end=" ")
        new_item = input().strip().lower()

        if not new_item:
            print("Error: Please enter a valid item name.")
            continue
        if new_item == "q":
            print("Bye!")
            break

        if new_item in grocery_list:
            print(
                f"{new_item.capitalize()} is already in your list. Remove it? (yes/no): ")
            if input().lower().strip() == "yes":
                grocery_list.remove(new_item)
                grocery_list.sort()
                print("\nUpdated list:")
                for item in grocery_list:
                    print(f"- {item.capitalize()}")
        else:
            grocery_list.append(new_item)
            grocery_list.sort()
            print("\nUpdated list:")
            for item in grocery_list:
                print(f"- {item.capitalize()}")


if __name__ == "__main__":
    list_organizer()
