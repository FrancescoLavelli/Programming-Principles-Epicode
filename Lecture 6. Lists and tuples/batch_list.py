"""**Add a batch list following from grocery list.
I just don't want to touche the other program/function
Or maybe I should try to use a lot of functions and put them altogether(one day)
"""
print("Please insert all ingredients separated by /")
batch_list = input(">>>").strip().split("/")
print(batch_list)
for item in batch_list:
    print(f"- {item.capitalize()}")
print([f"- {item.capitalize()}" for item in batch_list])
