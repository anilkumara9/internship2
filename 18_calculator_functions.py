# Professional Modular Calculator Functions
# This program implements arithmetic operations as discrete functions for scalability and clarity.

# Core Mathematical Functions
def addition(op1, op2):
    """Calculates the sum of two numbers."""
    return op1 + op2

def subtraction(op1, op2):
    """Calculates the difference between two numbers."""
    return op1 - op2

def multiplication(op1, op2):
    """Calculates the product of two numbers."""
    return op1 * op2

def division(op1, op2):
    """Returns the quotient. Handles division by zero internally."""
    if op2 == 0:
        return "Numerical Error: Division by zero is undefined."
    return op1 / op2

def calculate_modulus(op1, op2):
    """Returns the remainder of a division."""
    if op2 == 0:
        return "Numerical Error: Cannot calculate modulus with zero."
    return op1 % op2

def raise_to_power(base, exponent):
    """Calculates the power of a number."""
    return base ** exponent

def show_calculator_interface():
    """Presents a menu for the user to perform calculations."""
    print("\n--- MODULAR CALCULATOR TERMINAL ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    
    try:
        selection_option = input("Choose a mathematical operation (1-6): ")
        
        # Validating selection and gathering numbers
        if selection_option in ['1', '2', '3', '4', '5', '6']:
            val1 = float(input("Enter the first number: "))
            val2 = float(input("Enter the second number: "))
            
            # Mapping menu choice to specific function calls
            if selection_option == '1':
                print(f"Result: {val1} + {val2} = {addition(val1, val2)}")
            elif selection_option == '2':
                print(f"Result: {val1} - {val2} = {subtraction(val1, val2)}")
            elif selection_option == '3':
                print(f"Result: {val1} * {val2} = {multiplication(val1, val2)}")
            elif selection_option == '4':
                print(f"Result: {val1} / {val2} = {division(val1, val2)}")
            elif selection_option == '5':
                print(f"Result: {val1} % {val2} = {calculate_modulus(val1, val2)}")
            elif selection_option == '6':
                print(f"Result: {val1} ^ {val2} = {raise_to_power(val1, val2)}")
        else:
            print("Selection Error: Please enter a valid menu number (1-6).")

    except ValueError:
        print("Data Error: Please enter numerical values only for the operands.")

if __name__ == "__main__":
    show_calculator_interface()
