"""
    1 write a program to define a variable
    2 modify the value - same datatype
    3 modify datatype
    print var and datatype for each step
"""

# result = 10
# print(f"Definition: {result} Type: {type(result)}")
# result += 1
# print(f"Reassingment: {result} Type: {type(result)}")
# result = float(result)
# print(f"NewDataType: {result} Type: {type(result)}")

"""Implement find & replace
1 - Ask the use for word to be founded
    1.1 - And the replacement one
2 - Apply those substitutions to the chat text
3 - Print amended text
"""

quote = "Even the smallest person can change the course of the future."
quote_lower = quote.lower()
author = "J.R.R. Tolkien"


def text_amender() -> str:
    print(f"@\n{quote}\n@")
    print("\n>>>What would you like to modify?")
    discarded = input().lower()
    try:
        if discarded in quote:
            print("\n>>>Please insert the desired words: ")
            replaced = input()
        amended_quote = quote_lower.replace(discarded, replaced).title()
        print(f"\n@\n{amended_quote}\n@")
        print(f"\n>>>Did you do better then {author}?\n")
        print("Do you want to change something else?")
        new_amendment = input().lower()
        if new_amendment == "yes":
            amended_quote = amended_quote.lower.replace(
                discarded, replaced).title()
        elif new_amendment == "no":
            print("Bye")
        else:
            print("I'm sorry, I don't understand that. Yes or No?")
    except Exception:
        print("\n>>>Please, I can only modify words that are already in the text.\n")
        text_amender()


text_amender()
"""successive iterazioni aggiungi:
    
    the program finish after the if block, how can I loop thoruogh without a loop
    the program doesn't save the modification if I make mpre than 1
    try the libraries for yesno() input
    """
