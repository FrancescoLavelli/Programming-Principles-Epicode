def text_amender(quote: str, author: str = "Unknown") -> str:
    """Assignment
    1 write a program to define a variable
    2 modify the value - same datatype
    3 modify datatype
    print var and datatype for each step

    The function:
    Allows a user to make multiple amendments to a quote.

    Args:
        quote: The original quote to amend
        author: The author of the quote

    Returns:
        The final amended quote
    """
    # Keep track of the current version of the quote
    current_quote = quote

    while True:
        # Display the current quote
        print(f"\n\"\"\"\n{current_quote}\n\"\"\"")

        # Ask if the user wants to modify the quote
        print("\n>>>Do you want to modify something in the quote? (yes/no)")
        modify_choice = input().lower().strip()

        # Input costriction (if you put yes first, no never gonna happens)
        if modify_choice == "no":
            break
        elif modify_choice != "yes":
            print("\n>>> Sorry, please reply: (yes/no)")
            continue

        # Get the text to be replaced
        print("\n>>> What would you like to modify?")
        to_replace = input().strip()

        try:
            # Check if the text exists in the quote (case insensitive)
            current_quote_lower = current_quote.lower()
            to_replace_lower = to_replace.lower()

            if to_replace_lower not in current_quote_lower:
                print(
                    "\n>>> Sorry, I can only modify words that are already in the text.")
                continue

            # Get the replacement text
            print("\n>>> Please insert the desired words: ")
            replacement = input().strip()

            # Do the replacement (preserve case if possible)
            index = current_quote_lower.find(to_replace_lower)
            actual_text = current_quote[index:index + len(to_replace)]
            current_quote = current_quote.replace(actual_text, replacement)

            # Show the result
            print(f"\n\"\"\"\n{current_quote}\n\"\"\"")
            print(f"\n>>> Did you do better than {author}?\n")
        except Exception as e:
            print(f"\n>>> An error occurred: {e}")
            print("Let's try again.")

    print("\nFinal quote:")
    print(f"\n\"\"\"\n{current_quote}\n\"\"\"")
    return current_quote


# Example usage
if __name__ == "__main__":
    sample_quote = "Even the smallest person can change the course of the future."
    sample_author = "J.R.R. Tolkien"
    text_amender(sample_quote, sample_author)

"""
## Code Explanation:

This `text_amender` function allows users to make multiple amendments to a quote. Here's a detailed breakdown:

1. **Function Definition**:
- Takes two parameters: `quote` (required) and `author` (optional with default "Unknown")
- Returns the modified quote string

2. **Main Loop Structure**:
- Uses a `while True` loop to allow multiple amendments
- Each iteration displays the current state of the quote
- Asks the user if they want to modify the quote

3. **Input Validation**:
- Converts user input to lowercase and removes whitespace with `.lower().strip()`
- Has explicit handling for "yes", "no", and invalid inputs
- Continues the loop on invalid input with an error message

4. **Text Replacement Logic**:
- Gets the text to replace from user input
- Performs case-insensitive search by converting both the quote and search text to lowercase
- Validates that the text to replace exists in the quote
- Finds the exact case of the text in the original quote for proper replacement
- Replaces the text while preserving the structure of the rest of the quote

5. **Error Handling**:
- Uses try/except to catch any errors during the replacement process
- Provides clear error messages and allows the user to try again

6. **Output Formatting**:
- Uses triple quotes for displaying the quote
- Returns the final quote at the end

## Key Concept:
## Variable Scope and State Management

This pattern demonstrates an important programming concept: **state management**. 

- **Variables outside loops** maintain their values between iterations (persistent state)
- **Variables inside loops** are reinitialized on each iteration (temporary state)

By keeping `current_quote` outside the loop, we're creating a "memory" of all previous amendments, which is essential for the cumulative editing process that the function is designed to provide.

## Conclusion

The placement of `current_quote` outside the loop is intentional and necessary to fulfill the function's purpose of enabling multiple sequential amendments to a quote, where each amendment builds upon all previous changes.

## Future Improvements:

2. **Multi-word Replacement Enhancement**:
- The current implementation might have issues with replacing multiple instances of the same word
- Could add an option to replace all instances or just a specific one

3. **Input Validation Enhancement**:
- Add a retry limit for invalid inputs to prevent infinite loops

4. **Progress Tracking**:
- Add a counter to show how many amendments have been made

5. **History Feature**:
- Keep a history of changes to allow undoing previous amendments

6. **Save Functionality**:
- Add an option to save the final quote to a file

7. **Case Sensitivity Option**:
- Give the user the option to make case-sensitive replacements
"""
