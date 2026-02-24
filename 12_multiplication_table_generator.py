# Dynamic Multiplication Table Generator
# This program creates tables for specific numbers and a full 1-10 reference grid.

try:
    # Collecting table parameters from user
    target_multiplicand = int(input("Enter the number for the multiplication table: "))
    table_limit = int(input("Enter the range limit (e.g., 10 or 20): "))

    # Generating the specific multiplication table
    print(f"\n--- Multiplication Table of {target_multiplicand} ---")
    for multiplier in range(1, table_limit + 1):
        product_result = target_multiplicand * multiplier
        print(f"{target_multiplicand} x {multiplier} = {product_result}")

    # Generating a formatted 10x10 multiplication grid for reference
    print("\n--- Bonus: 1 to 10 Multiplication Grid ---")
    # Header row
    for col_header in range(1, 11):
        print(f"{col_header:4}", end="")
    print("\n" + "═" * 40)

    # Grid content
    for row_val in range(1, 11):
        for col_val in range(1, 11):
            cell_product = row_val * col_val
            # Formatting with 4 characters width for alignment
            print(f"{cell_product:4}", end="")
        print()

except ValueError:
    # Handling non-integer inputs gracefully
    print("Invalid Input: Please enter integer values for the calculations.")
except Exception as unexpected_error:
    print(f"An unexpected error occurred: {unexpected_error}")
