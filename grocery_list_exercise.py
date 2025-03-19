""" **Grocery List
#1 create a grocery list
#2 Sort alphab
#4 print: "-item_list"
#5 ask user to add new article
#6 if empty insert raise error message
#7 if insert existing article raise error message
#8 if correct addd article to list
#9 print new list in alphabetical order
"""


grocery_list = ["carrot", " broccoli", "fennel", "bread",
                "hummus", "fish", "mince", "Bananas", "blueberries"]  # 1


def list_organizer():
    grocery_list.sort()  # 2
    for groceries in grocery_list:
        print(f"- {groceries}")  # 4
    grocery_string = " ".join(grocery_list)
    # Remove whitespace character. I accidentally typed a space before Broccoli
    grocery_string.strip()
    comparable_list = grocery_string.lower().split(" ")
    print(grocery_string.lower().split(" "))

    while True:
        print("What do you want to buy today?\nTo Exit press: \"Q\" \n$$$:", end="")  # 5
        new_item = input().strip()

        if not new_item:
            # 6 I put False and it didn't work then i put " " but it didn't work either was adding the empty element to the list WHY?
            print("Please add an item.")
            continue
        elif new_item.lower() in comparable_list:
            print(
                # 7
                f"{new_item} is already in your list. Do you want to remove from the list?: Yes/No ")
            answer = input().lower().strip()
            if answer == "yes":
                comparable_list.remove(new_item)
                print(comparable_list)
                continue
        elif new_item.lower() == "q":
            print("Bye")
            break
        else:
            if new_item.lower() not in comparable_list:  # 8
                comparable_list.append(new_item)
                comparable_list.sort()
                print(comparable_list)  # 9


if __name__ == "__main__":
    list_organizer()
