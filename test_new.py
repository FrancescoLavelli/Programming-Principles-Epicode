def debug_exercise():
    print("\n=== DEBUG: Starting exercise function ===")
    count = 0

    print("Beginning while loop...")
    while count < 4:
        count += 1
        print(f"\nIteration {count} of 4 ===")

        # Explicitly prompt for input
        print(f"Please enter input #{count} (then press Enter):")

        try:
            # Capture raw input with explicit prompt text
            print(">>> ", end="")  # Print prompt without newline
            raw_input = input()
            print(
                f"Raw input received: '{raw_input}' (type: {type(raw_input).__name__})")

            # Check if input is somehow a tuple (which would be unusual)
            if isinstance(raw_input, tuple):
                print(f"DEBUG: WARNING! Input is a tuple: {raw_input}")

            # Original print statement
            print(f"Var: {raw_input} Type: {type(raw_input)}")

        except Exception as e:
            print(f"DEBUG: ERROR during input processing: {e}")
            print(f"DEBUG: Error type: {type(e).__name__}")

    print("\n=== DEBUG: Loop complete ===")


if __name__ == "__main__":
    print("=== DEBUG: Program starting ===")
    print("DEBUG: About to call debug_exercise()")
    result = debug_exercise()
    print("\n=== DEBUG: Function completed! ===")
    print(f"DEBUG: Final result: '{result}' (type: {type(result).__name__})")

    # Additional diagnostics
    print("\nDEBUG: Diagnostic information:")
    print(f"Python version: {__import__('sys').version}")
    print(f"Running in terminal: {__import__('sys').stdout.isatty()}")
