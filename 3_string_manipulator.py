# String Manipulation Program
# This program analyzes user-input sentences and performs various string operations.

user_sentence = input("Enter a sentence: ")

# Splitting the sentence into a list of words for further analysis
word_list = user_sentence.split()

# Displaying basic string properties
print(f"Original Sentence: {user_sentence}")
print(f"Total Characters (with spaces): {len(user_sentence)}")
print(f"Total Characters (without spaces): {len(user_sentence.replace(' ', ''))}")
print(f"Total Word Count: {len(word_list)}")

# Displaying case variations
print(f"UPPERCASE Format: {user_sentence.upper()}")
print(f"lowercase Format: {user_sentence.lower()}")
print(f"Title Case Format: {user_sentence.title()}")

# Displaying specific word positions if the sentence is not empty
if word_list:
    print(f"The first word is: {word_list[0]}")
    print(f"The last word is: {word_list[-1]}")
else:
    print("No words found to display positions.")

# Reversing the string using slicing
print(f"Reversed Sentence: {user_sentence[::-1]}")
