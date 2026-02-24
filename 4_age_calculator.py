# Comprehensive Age Calculator
# This program calculates age in various time units based on the birth year.

import datetime

try:
    # Fetching the current year dynamically using the datetime module
    current_year = datetime.datetime.now().year
    birth_year = int(input("Enter your birth year (e.g., 1995): "))

    # Checking if the birth year is valid (not in the future)
    if birth_year > current_year:
        print("The birth year cannot be in the future.")
    else:
        # Calculating age in different units
        current_age = current_year - birth_year
        age_in_months = current_age * 12
        age_in_days = current_age * 365
        age_in_hours = age_in_days * 24
        age_in_minutes = age_in_hours * 60
        years_remaining_to_100 = 100 - current_age

        # Displaying the calculated breakdown with comma formatting for readability
        print(f"\n--- Age Analysis (Reference Year: {current_year}) ---")
        print(f"Current age      : {current_age} years")
        print(f"Age in months    : {age_in_months:,} months")
        print(f"Age in days      : {age_in_days:,} days (approximate)")
        print(f"Age in hours     : {age_in_hours:,} hours")
        print(f"Age in minutes   : {age_in_minutes:,} minutes")
        
        if years_remaining_to_100 > 0:
            print(f"Years until 100  : {years_remaining_to_100} years")
        else:
            print("Congratulations on reaching/passing 100 years!")

except ValueError:
    # Handling non-integer inputs for birth year
    print("Invalid Input: Please enter a valid integer for the birth year.")
except Exception as error_message:
    # General error handling
    print(f"An error occurred: {error_message}")
