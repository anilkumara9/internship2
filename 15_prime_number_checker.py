# Prime Number Utility Tool
# This program identifies individual prime numbers and lists primes within a specified range.

def check_primality(test_number):
    """Returns True if the test_number is prime, otherwise False."""
    if test_number <= 1:
        return False
    # Only checking up to the square root of n for efficiency
    for divisor in range(2, int(test_number**0.5) + 1):
        if test_number % divisor == 0:
            return False
    return True

try:
    # PART 1: Single Number Check
    single_value = int(input("Enter a number to check for primality: "))
    if check_primality(single_value):
        print(f"Status: {single_value} is a Prime Number.")
    else:
        print(f"Status: {single_value} is NOT a Prime Number.")

    # PART 2: Range-Based Search
    print("\n--- PRIME RANGE FINDER ---")
    range_start = int(input("Enter start of the search range: "))
    range_end = int(input("Enter end of the search range: "))

    if range_start > range_end:
        print("Range Error: Start value must be less than or equal to the end value.")
    else:
        # Building a list of primes using list comprehension and our helper function
        discovered_primes = [num for num in range(range_start, range_end + 1) if check_primality(num)]
        
        print(f"Discovered {len(discovered_primes)} Primes in range [{range_start} to {range_end}]:")
        if discovered_primes:
            print(discovered_primes)
        else:
            print("No prime numbers were found in this range.")

except ValueError:
    print("Invalid Input: Primality checks require integer values.")
except Exception as sys_error:
    print(f"A system error occurred: {sys_error}")
