# Integrated Mathematical Number System functions
# This program provides a wide array of mathematical tools and sequence generators.

def calculate_factorial(num):
    """Iteratively computes the factorial for non-negative integers."""
    if num < 0: return "undefined for negative values"
    if num == 0: return 1
    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result *= i
    return factorial_result

def evaluate_primality(num):
    """Determines if a number has exactly two distinct divisors."""
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def generate_fibonacci_sequence(length):
    """Generates the fibonacci sequence up to the desired length."""
    if length <= 0: return []
    if length == 1: return [0]
    sequence_list = [0, 1]
    while len(sequence_list) < length:
        # Summing the last two elements
        sequence_list.append(sequence_list[-1] + sequence_list[-2])
    return sequence_list

def calculate_sum_of_digits(num):
    """Sums the individual integer digits of any number."""
    return sum(int(digit) for digit in str(abs(num)))

def flip_number_digits(num):
    """Reverses the order of digits while preserving the sign."""
    is_negative = -1 if num < 0 else 1
    reversed_digit_str = str(abs(num))[::-1]
    return is_negative * int(reversed_digit_str)

def check_armstrong_property(num):
    """True if sum of digits raised to the power of number of digits equals the number."""
    data_digits = [int(d) for d in str(abs(num))]
    num_of_digits = len(data_digits)
    sum_of_powers = sum(d**num_of_digits for d in data_digits)
    return num == sum_of_powers

def find_gcd(val1, val2):
    """Calculates Greatest Common Divisor using Euclidean Algorithm."""
    while val2:
        val1, val2 = val2, val1 % val2
    return val1

def find_lcm(val1, val2):
    """Calculates Least Common Multiple based on GCD."""
    if val1 == 0 or val2 == 0: return 0
    return abs(val1 * val2) // find_gcd(val1, val2)

def is_mathematically_perfect(num):
    """True if the sum of all proper divisors equals the number itself."""
    if num < 1: return False
    divisors_found = [i for i in range(1, num) if num % i == 0]
    return sum(divisors_found) == num

def launch_math_dashboard():
    """Provides an interactive CLI interface for math functions."""
    while True:
        print("\n--- ADVANCED MATHEMATICAL DASHBOARD ---")
        print("1. Factorial Calculator")
        print("2. Primality Verification")
        print("3. Fibonacci Generator")
        print("4. Sum of Individual Digits")
        print("5. Digits Reversal")
        print("6. Armstrong Number Check")
        print("7. Find GCD (two numbers)")
        print("8. Find LCM (two numbers)")
        print("9. Perfect Number Verification")
        print("0. Terminate Dashboard")
        
        try:
            menu_selection = input("\nEnter your command (0-9): ")
            if menu_selection == '0':
                print("Dashboard closed. Have a productive day!")
                break
            
            # Grouping single-input functions
            if menu_selection in ['1', '2', '3', '4', '5', '6', '9']:
                target_value = int(input("Enter target number: "))
                
                if menu_selection == '1': print(f"Factorial of {target_value}: {calculate_factorial(target_value)}")
                elif menu_selection == '2': print(f"Is {target_value} Prime?: {evaluate_primality(target_value)}")
                elif menu_selection == '3': print(f"Fibonacci Sequence ({target_value} items): {generate_fibonacci_sequence(target_value)}")
                elif menu_selection == '4': print(f"Sum of digits in {target_value}: {calculate_sum_of_digits(target_value)}")
                elif menu_selection == '5': print(f"Reversed digits of {target_value}: {flip_number_digits(target_value)}")
                elif menu_selection == '6': print(f"Is {target_value} Armstrong?: {check_armstrong_property(target_value)}")
                elif menu_selection == '9': print(f"Is {target_value} a Perfect Number?: {is_mathematically_perfect(target_value)}")
            
            # Dual-input functions
            elif menu_selection in ['7', '8']:
                input_a = int(input("Enter first number (Integer A): "))
                input_b = int(input("Enter second number (Integer B): "))
                if menu_selection == '7': print(f"GCD of {input_a} and {input_b}: {find_gcd(input_a, input_b)}")
                elif menu_selection == '8': print(f"LCM of {input_a} and {input_b}: {find_lcm(input_a, input_b)}")
            else:
                print("Dashboard Error: Command not recognized.")
                
        except ValueError:
            print("Input Error: Please provide integer values for calculations.")
        except Exception as system_ex:
            print(f"Dashboard Runtime Error: {system_ex}")

if __name__ == "__main__":
    launch_math_dashboard()
