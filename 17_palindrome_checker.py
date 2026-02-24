# Palindrome Verification Suite
# This program checks if a string or number reads the same forwards and backwards.

def run_palindrome_checker():
    """Takes user input and determines if it is a palindrome."""
    raw_user_input = input("Enter a word, sentence, or number to check: ")
    
    # Data Cleaning: Removing spaces and converting to lowercase for accurate comparison
    # '123 21' should be treated as '12321'
    processed_string = str(raw_user_input).lower().replace(" ", "")
    
    # Reversing the processed string using stepping notation
    reversed_sequence = processed_string[::-1]
    
    print(f"\nAnalysis for: '{raw_user_input}'")
    print(f"Standardized Seq: {processed_string}")
    print(f"Reversed Sequence: {reversed_sequence}")
    
    # Final Comparison Logic
    if processed_string == reversed_sequence:
        print("Final Verdict: This input is a valid Palindrome!")
    else:
        print("Final Verdict: This input is NOT a palindrome.")

if __name__ == "__main__":
    try:
        run_palindrome_checker()
    except Exception as unexpected_error:
        print(f"A processing error occurred: {unexpected_error}")
    finally:
        print("\nThank you for using the Palindrome Checker.")
