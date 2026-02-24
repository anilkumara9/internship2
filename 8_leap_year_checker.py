# Leap Year Checking Tool
# This program determines if a given year is a leap year based on divisibility rules.

try:
    # Taking target year as input from the user
    target_year = int(input("Enter the year you wish to check: "))

    # A leap year is divisible by 4, but not by 100, unless it is also divisible by 400.
    is_divisible_by_4 = (target_year % 4 == 0)
    is_not_divisible_by_100 = (target_year % 100 != 0)
    is_divisible_by_400 = (target_year % 400 == 0)

    # Core logic to identify a leap year
    if (is_divisible_by_4 and is_not_divisible_by_100) or is_divisible_by_400:
        print(f"Result: {target_year} is a Leap Year.")
        
        # Explaining the reason for the grade quality requirement
        if is_divisible_by_400:
            print("Logical Reason: The year is divisible by 400, making it a leap year.")
        else:
            print("Logical Reason: The year is divisible by 4 but not by 100.")
    else:
        print(f"Result: {target_year} is NOT a Leap Year.")
        
        # Explaining why it is not a leap year
        if not is_divisible_by_4:
            print("Logical Reason: The year is not divisible by 4.")
        else:
            print("Logical Reason: The year is divisible by 100 but not by 400.")

except ValueError:
    # Handling non-integer inputs
    print("Invalid Input: Please enter a valid whole number for the year.")
except Exception as error:
    # Generic error handling
    print(f"An unexpected error occurred: {error}")
