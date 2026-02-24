# Restaurant Bill Splitter
# This program calculates the total bill inclusive of tax and tip, and splits it among guests.

try:
    # Collecting financial details from the user
    subtotal_bill = float(input("Enter the total bill amount (before tax): "))
    guest_count = int(input("Enter the number of people to split with: "))
    tax_rate = float(input("Enter the tax percentage (e.g., 5 for 5%): "))
    tip_rate = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

    # Validating that at least one person is paying
    if guest_count <= 0:
        print("Error: Number of people must be greater than zero.")
    else:
        # Calculating tax and intermediate values
        calculated_tax = (tax_rate / 100) * subtotal_bill
        amount_after_tax = subtotal_bill + calculated_tax
        
        # Calculating tip based on the subtotal plus tax
        calculated_tip = (tip_rate / 100) * amount_after_tax
        final_total_bill = amount_after_tax + calculated_tip
        cost_per_individual = final_total_bill / guest_count

        # Displaying the detailed financial breakdown
        print("\n--- FINAL BILL BREAKDOWN ---")
        print(f"Subtotal Amount       : ₹{subtotal_bill:.2f}")
        print(f"Applied Tax ({tax_rate}%)   : ₹{calculated_tax:.2f}")
        print(f"Total After Tax       : ₹{amount_after_tax:.2f}")
        print(f"Applied Tip ({tip_rate}%)   : ₹{calculated_tip:.2f}")
        print(f"Grand Total Bill      : ₹{final_total_bill:.2f}")
        print("-" * 28)
        print(f"Share Per Person      : ₹{cost_per_individual:.2f}")

except ValueError:
    # Handling cases where numerical input is expected but not received
    print("Invalid Input: Please enter numeric values for bill, tax, and counts.")
except ZeroDivisionError:
    # Robustness against dividing by zero people
    print("Error: Cannot divide the bill by zero people.")
except Exception as error:
    # General error capture
    print(f"An unexpected error occurred: {error}")
