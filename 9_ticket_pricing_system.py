# Professional Movie Ticket Pricing System
# This program calculates ticket costs based on age and weekend discount policies.

try:
    # Capturing user data for pricing calculation
    viewer_age = int(input("Please enter your Age: "))
    day_of_session = input("Enter the Day of the week: ").strip().capitalize()
    ticket_quantity = int(input("How many tickets would you like to purchase?: "))

    # Validating basic business constraints
    if viewer_age < 0 or ticket_quantity <= 0:
        print("Input Error: Age cannot be negative and ticket count must be at least 1.")
    else:
        # Base pricing logic based on age brackets
        if viewer_age < 3:
            standard_base_price = 0  # Infants enter free
        elif 3 <= viewer_age <= 12:
            standard_base_price = 150  # Child rate
        elif 13 <= viewer_age <= 59:
            standard_base_price = 300  # Adult rate
        else:
            standard_base_price = 200  # Senior citizen rate

        # Applying a 20% discount if the booking is for the weekend (Friday, Saturday, Sunday)
        active_discount_amount = 0
        weekend_days = ["Friday", "Saturday", "Sunday"]
        
        if day_of_session in weekend_days:
            # 20% discount on the base price
            active_discount_amount = 0.20 * standard_base_price

        # Calculating final pricing
        discounted_ticket_price = standard_base_price - active_discount_amount
        total_payment_required = discounted_ticket_price * ticket_quantity

        # Presenting the final ticket invoice
        print(f"\n--- TICKET BOOKING INVOICE ---")
        print(f"Category Base Price     : ₹{standard_base_price}")
        print(f"Weekend Discount Applied: ₹{active_discount_amount:.2f}")
        print(f"Price Per Ticket (Final): ₹{discounted_ticket_price:.2f}")
        print("-" * 31)
        print(f"TOTAL AMOUNT PAYABLE    : ₹{total_payment_required:.2f}")

except ValueError:
    # Error handling for numeric fields
    print("Invalid Input: Please ensure Age and Ticket Quantity are entered as numbers.")
except Exception as general_error:
    # General fallback for unexpected runtime issues
    print(f"A processing error occurred: {general_error}")
