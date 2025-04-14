clients = ["Luisa", "Mario", "Pino", "Anna"]

clients.sort()  # c'e' anche la funzione sorted() ma va a creare un'altra lista
clients.append("Putu")
clients.extend(["Gianni", "Guido", "Luigi"])
clients.remove("Pino")
clients.pop(3)
# clients.copy()  # This means it creates a new list object with the same elements as the original list.
clients.count("Gianni")
clients.index("Anna")
clients.insert(-2, "Luigi")
clients.reverse()
# clients.clear()
# clients.__add__  # che fa?

# this way a create a new list, if i put only female_clients = clients I just give 2 names to the same variable that pointing at the same space in memory.
female_clients = clients[:]
female_clients = clients.copy()  # or .copy() method does the same thing
female_clients.remove("Mario")
# female_clients.remove("Pino")

for client in clients:
    print(client)
print(clients)
print(len(clients))

# List Comprehension
new_list = [client for client in clients if len(client) < 5]
# posso anche omettere la condizione ed usare qualche metodo o both, perche' e'  e  ritorna una stringa
new_list = [client.lower() for client in clients]
print(new_list)

name = "Homer Simpson"
name_list = list(name)  # crea una lista con elementi i caratteri della stringa
name_list.remove("m")
print(type(name_list), name_list)
# I cannot use .sort() method on a str but i can sort it with the sorted() function
print(sorted(name))

ingredients = ["butter", "jelly", "bread"]
sandwich = " & ".join(ingredients)
print(sandwich)  # butter & jelly & bread
# The method get me back a list, I pass the separator to split the elements in the string
print(sandwich.split(" & "))

# ** Tuple **
# useful for a group of elements that does not have sense to modify like days of the week

(a, b, c) = (5, 10, 7)  # tuple unpacking, I can omit ()
