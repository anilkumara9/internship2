# Basic Simple Calculator
# This program performs addition, subtraction, multiplication, division, modulus, and exponentiation.

try:
    # Taking numerical inputs from the user
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    # Displaying results of arithmetic operations
    print("\n--- Calculation Results ---")
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")

    # Handling division and modulus by checking for zero to avoid Runtime Errors
    if second_number != 0:
        print(f"{first_number} / {second_number} = {round(first_number / second_number, 2)}")
        print(f"{first_number} % {second_number} = {first_number % second_number}")
    else:
        print("Division/Modulus: Error (Cannot divide by zero)")

    print(f"{first_number} raised to power {second_number} = {first_number ** second_number}")

except ValueError:
    # Handling cases where the user inputs non-numeric values
    print("Invalid Input: Please enter numerical values only.")
except Exception as e:
    # Catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")
