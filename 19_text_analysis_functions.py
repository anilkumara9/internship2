# Comprehensive Text Analysis Utility
# This program provides multiple functions to dissect and analyze text properties and frequency.

def get_word_count(input_string):
    """Splits string by whitespace to get total word count."""
    return len(input_string.split())

def get_vowel_count(input_string):
    """Counts vowels (A, E, I, O, U) in the provided text."""
    vowel_set = "aeiouAEIOU"
    return len([char for char in input_string if char in vowel_set])

def get_consonant_count(input_string):
    """Counts alphabetic characters that are not vowels."""
    vowel_set = "aeiouAEIOU"
    return len([char for char in input_string if char.isalpha() and char not in vowel_set])

def reverse_string_sequence(input_string):
    """Flips the string sequence entirely."""
    return input_string[::-1]

def verify_if_palindrome(input_string):
    """Checks if the text is a palindrome (ignores case and spaces)."""
    sanitized_text = input_string.lower().replace(" ", "")
    return sanitized_text == sanitized_text[::-1]

def strip_vowels_from_text(input_string):
    """Returns a copy of the text with all vowels removed."""
    vowel_set = "aeiouAEIOU"
    return "".join([char for char in input_string if char not in vowel_set])

def calculate_word_frequency(input_string):
    """Maps each unique word to its number of occurrences."""
    words_processed = input_string.lower().split()
    frequency_map = {}
    for word in words_processed:
        # Standardizing word keys
        clean_word = word.strip(".,!?")
        frequency_map[clean_word] = frequency_map.get(clean_word, 0) + 1
    return frequency_map

def locate_longest_word(input_string):
    """Identifies the word with the maximum character length."""
    tokens = input_string.split()
    if not tokens: return "None Found"
    return max(tokens, key=len)

def perform_comprehensive_analysis(sample_text):
    """Prints a detailed report of all analyzer functions."""
    print("\n--- TEXT ANALYSIS METRIC REPORT ---")
    print(f"Source Text: \"{sample_text}\"")
    print("-" * 35)
    print(f"Total Word Count    : {get_word_count(sample_text)}")
    print(f"Vowel Count       : {get_vowel_count(sample_text)}")
    print(f"Consonant Count   : {get_consonant_count(sample_text)}")
    print(f"Reversed Layout   : \"{reverse_string_sequence(sample_text)}\"")
    print(f"Is Palindrome     : {verify_if_palindrome(sample_text)}")
    print(f"Consonants Only   : \"{strip_vowels_from_text(sample_text)}\"")
    print(f"Word Frequency    : {calculate_word_frequency(sample_text)}")
    print(f"Longest Word Found: \"{locate_longest_word(sample_text)}\"")

if __name__ == "__main__":
    try:
        raw_text_entry = input("Enter a string for detailed analysis: ")
        if not raw_text_entry.strip():
            print("Warning: Input is empty. Resulting metrics may be trivial.")
        perform_comprehensive_analysis(raw_text_entry)
    except Exception as analysis_exception:
        print(f"An error occurred during text processing: {analysis_exception}")
