"""Print on terminal, 1 below another, the 3 main characters from the movie
    "Tre Umoni e Una Gamba". Use only positional argument
"""
#Sol 1
print("Aldo")
print("Giovanni")
print("Giacomo")

#Sol 2
print("Aldo\nGiovanni\nGiacomo")

# shift+opt+down or up to duplicate down or up         ⇧⌥↓ / ⇧⌥↑ Copy line down/up
# Home / End    Go to beginning/end of line
# ⌘↑ / ⌘↓       Go to beginning/end of file
# ⇧⌘↑ / ⇧⌘↓     To select all till the Top/Bottom
# ⌘L+⌘L Select current line


#Sol 3 with  Keyword Argument
print("Aldo", "Giovanni", "Giacomo", sep="\n")
print("Aldo", "Giovanni", "Giacomo", sep="\n")
print("Aldo", "Giovanni", "Giacomo", sep="\n")


"""
now print must look like this:
Aldo,Giovanno,Giacomo.
"""

#Sol 1
print("Aldo,", "Giovanni,", "Giacomo.", sep="")
#Best Sol
print("Aldo", "Giovanni", "Giacomo", sep=",", end=".")

"""Only 1 function Print. 
Jacqueline>Marge>Lisa
Positional arguments must not containt > charater
"""

#Sol 1
print("Jacqueline", "Marge", "Lisa", sep=">") #remember sep acts only between arguments
#multicursor command       ⌥ + click Insert cursor

"""generate 4 syntax errors and 
                   4 runtime errors"""

"""print(name)
print(surname)
print(age)
input(age)
pippo()
print("J)
print("k
print("l
print("m" """

"""Take user name
store it pass to the function and print ut
Nome Utente = MyName"""

#Sol 1
print("Hello, what's your Name?")
username = input()
print("Username", username, sep=" = ")

#Sol 2
username = input("Hello, what's your Name?\n")
print("Username", username, sep=" = ")

"""do it without variables"""

print("Username", input("Hello, what's your Name?\n"))  #python interpeter solve the second argument first because is not defined


print("lala") #cursorWordLeftSelect shift + opt + ->   ⇧ ⌥ →



import this