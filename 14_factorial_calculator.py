# Step-by-Step Factorial Calculator
# This program calculates the factorial of a number and shows the multiplication process.

try:
    # Taking target number for factorial calculation
    target_input = int(input("Enter a positive whole number: "))

    # Mathematical Rule: Factorial is not defined for negative integers
    if target_input < 0:
        print("Mathematical Error: Factorial is only defined for non-negative integers.")
    elif target_input == 0:
        # Special Case: 0! = 1
        print("Result: 0! = 1")
    else:
        calculated_factorial = 1
        visual_process_steps = ""
        
        # Iteratively calculating the factorial and building the visualization string
        for current_val in range(target_input, 0, -1):
            calculated_factorial *= current_val
            visual_process_steps += str(current_val)
            
            # Appending 'x' separator for all but the last digit
            if current_val > 1:
                visual_process_steps += " x "
        
        # Final result presentation
        print(f"\nCalculation Logic: {target_input}! = {visual_process_steps}")
        print(f"Final Factorial Product: {calculated_factorial}")

except ValueError:
    # Handling non-integer inputs
    print("Invalid Input: Please provide a valid integer for the factorial calculation.")
except Exception as general_err:
    print(f"An unexpected error occurred: {general_err}")
