# Simulated Automated Teller Machine (ATM)
# This program simulates basic banking operations like balance check, deposit, and withdrawal.

def run_atm_simulator():
    """Simulates a simple ATM interface."""
    current_account_balance = 10000.0  # Starting balance
    MINIMUM_MAINTAINABLE_BALANCE = 500.0  # Business rule: balance cannot drop below this

    while True:
        print("\n--- SECURE ATM SIMULATOR ---")
        print("1. Check Account Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit Terminal")
        
        user_selection = input("Please select an operation (1-4): ")
        
        if user_selection == '1':
            # Display current balance
            print(f"Your current account balance is: ₹{current_account_balance:,.2f}")
            
        elif user_selection == '2':
            # Handle deposits
            try:
                deposit_amt = float(input("Enter the amount you wish to deposit: "))
                if deposit_amt > 0:
                    current_account_balance += deposit_amt
                    print(f"Transaction Successful! Your new balance is: ₹{current_account_balance:,.2f}")
                else:
                    print("Error: Deposit amount must be a positive value.")
            except ValueError:
                print("Invalid Input: Please enter a numerical value for the deposit.")
                
        elif user_selection == '3':
            # Handle withdrawals with logic for minimum balance
            try:
                withdrawal_amt = float(input("Enter the amount you wish to withdraw: "))
                
                if withdrawal_amt <= 0:
                    print("Error: Withdrawal amount must be positive.")
                elif (current_account_balance - withdrawal_amt) < MINIMUM_MAINTAINABLE_BALANCE:
                    print(f"Transaction Denied! Withdrawing ₹{withdrawal_amt} would drop your balance below")
                    print(f"the required minimum of ₹{MINIMUM_MAINTAINABLE_BALANCE}.")
                else:
                    current_account_balance -= withdrawal_amt
                    print(f"Transaction Successful! Please collect your cash.")
                    print(f"Your remaining balance is: ₹{current_account_balance:,.2f}")
            except ValueError:
                print("Invalid Input: Please enter a numerical value for the withdrawal.")
                
        elif user_selection == '4':
            # Terminating session
            print("Thank you for using our ATM services. Have a great day!")
            break
        else:
            # Handling invalid menu choices
            print("Selection Error: Please choose a valid menu option (1-4).")

# Starting the simulation
if __name__ == "__main__":
    run_atm_simulator()
