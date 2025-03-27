"""***Assignment
    1.Transform list to dic
    2.dic must contains:
        key:product, value: its quantity
    3.user will be required to input product and quantity
    4.do not need to order dictionary
    5.Bonus. If article in dictionary, ask  to update quantity
"""
items = ["beans", "nuts", "apple"]
values = [10, 5, 15]

""" 2 listes case"""
# if you have 2 lists you can use .zip()
# new_dict = dict(zip(items, values))
# print(new_dict)


for_dict = {item: " " for item in items}
print(f"Type: {type(for_dict)}, Dictionary: {for_dict}")


new_item = input("Please insert: 'item'\n >>>")

if new_item in for_dict:
    new_item_quantity = input("Please update 'quantity'\n >>>")
else:
    new_item_quantity = input("Please insert: 'quantity'\n >>>")

for_dict[new_item] = new_item_quantity

print(for_dict)

# double click + right click (Rename Symbol) or F2 to modify the variable name

""" Prof Solution"""

items = {
    "coffee": 5,
    "beans": 10,
    "apples": 15,
}

for item, quantity in items.items():  # EXPLAIN EXPLAIN EXPLAIN why I have to call .items()
    print(f"- {item} ({quantity} pezzi)")

user_item = input("Add an article: ").lower().strip()

if not user_item:
    print("Error: Please insert at least 1 article")
elif user_item in items:
    print("Error: article in already in use")
else:
    user_quantity = int(input("Insert quantity: ").strip())
    items[user_item] = user_quantity
    print("Article added ✅")

for item, quantity in items.items():
    print(f"- {item} ({quantity} pezzi)")
