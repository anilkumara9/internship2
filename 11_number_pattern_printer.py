# Number Pattern Printer Application
# This program generates four distinct numerical patterns based on user choice and desired height.

def generate_patterns():
    """Provides a menu to print various numerical patterns."""
    print("Available Patterns:")
    print("1. Incremental Right Triangle (1, 12, 123...)")
    print("2. Same Number per Row Triangle (1, 22, 333...)")
    print("3. Inverted Countdown Triangle (54321, 4321...)")
    print("4. Centered Pyramid Pattern (1, 121, 12321...)")

    try:
        # Taking pattern choice and grid height from user
        user_choice = int(input("\nEnter your selection (1-4): "))
        grid_height = int(input("Enter desired pattern height: "))

        if grid_height <= 0:
            print("Configuration Error: Height must be a positive integer.")
            return

        # Executing the logic for the selected pattern
        if user_choice == 1:
            for row in range(1, grid_height + 1):
                for column in range(1, row + 1):
                    print(column, end=" ")
                print()  # New line after each row
                
        elif user_choice == 1:
            # Pattern 1: Right-angle triangle incrementing columns
            for i in range(1, grid_height + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()
                
        elif user_choice == 2:
            # Pattern 2: Right-angle triangle repeating the row number
            for i in range(1, grid_height + 1):
                for j in range(1, i + 1):
                    print(i, end=" ")
                print()
                
        elif user_choice == 3:
            # Pattern 3: Inverted triangle counting down
            for i in range(grid_height, 0, -1):
                for j in range(i, 0, -1):
                    print(j, end=" ")
                print()
                
        elif user_choice == 4:
            # Pattern 4: Symmetrical pyramid pattern
            for i in range(1, grid_height + 1):
                # Leading spaces for alignment
                print(" " * (grid_height - i), end="")
                # Incremental part
                for j in range(1, i + 1):
                    print(j, end="")
                # Decremental part
                for j in range(i - 1, 0, -1):
                    print(j, end="")
                print()
        else:
            print("Selection Error: Please choose a valid pattern number (1-4).")

    except ValueError:
        print("Invalid Input: Please enter integers for selection and height.")

if __name__ == "__main__":
    generate_patterns()
