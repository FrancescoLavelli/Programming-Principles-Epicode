""" Data Persistance
data creation 
data access
"""

# to create file in our HD
# first argument is the name with relative path, second is writing mode, encoding must be inserted "utf-8" the default is "cp1252"
# open function generate a stream channel, where data flows and gives back and object
item_to_buy = input

# file = open("grocery_list.txt", "w", encoding="utf-8")
# file.write("Blueberries")
# file.write(item_to_buy)
# write override anything is in the file and create it if is not present
# file.close()
# with = context manager to open and close automatically
# with open("grocery_list.txt", "w", encoding="utf-8") as file:
#     file.write(item_to_buy)
# append to add not override we need to add the spacing. It creats the file if it does not exist
# with open("grocery_list.txt", "a", encoding="utf-8", newline="\n") as file:
#     file.write(item_to_buy + "\n")
# read does not create a new file   with method size  Ican read how many characters we can read
# with open("grocery_list.txt", "r", encoding="utf-8") as file:
#     file.read()
# readline() gives back single line (of bytes) but of text too. Sequential access
# readlines() gives bak a list, read a string
# writelines([item, item, item]) we can write a list

# nowadays we use libraries to access, write and modify files

# binary files you need to add b in the mode
with open("/Users/francescolavelli/Downloads/Jordan_Ghibli.jpg", "rb") as file:
    image_data_lines = file.readlines()

print(len(image_data_lines))
print(type(image_data_lines))
print(type(image_data_lines[0]))

# I can copy the file this way
with open("/Users/francescolavelli/Downloads/Jordan_Ghibli_2.jpg", "wb") as file:
    for line in image_data_lines:
        file.write(line)

# partial copy
with open("/Users/francescolavelli/Downloads/Jordan_Ghibli_2.jpg", "wb") as file:
    for line in image_data_lines[0:200]:
        file.write(line)

# sequential access vs random access
with open("grocery_list.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

with open("grocery_list.txt", "r", encoding="utf-8") as file:
    file.seek(2)  # we say where to start
    print(file.read(20))  # for how many characters
    file.seek(10)
    print(file.read(10))
