# Temperature Conversion Application
# This program provides a menu-driven interface to convert between Celsius, Fahrenheit, and Kelvin.

def start_temperature_converter():
    """Main function to handle temperature conversion logic."""
    while True:
        print("\n--- TEMPERATURE CONVERTER MENU ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit Application")
        
        user_choice = input("Select a conversion option (1-7): ")
        
        # Checking if user wants to exit
        if user_choice == '7':
            print("Thank you for using the Temperature Converter!")
            break
            
        # Validating menu selection
        if user_choice in ['1', '2', '3', '4', '5', '6']:
            try:
                # Taking temperature input and handling potential errors
                input_temp = float(input("Enter temperature value to convert: "))
                
                # Performing conversion based on user selection
                if user_choice == '1':
                    result_temp = (input_temp * 9/5) + 32
                    print(f"Result: {input_temp} C = {result_temp:.2f} F")
                elif user_choice == '2':
                    result_temp = (input_temp - 32) * 5/9
                    print(f"Result: {input_temp} F = {result_temp:.2f} C")
                elif user_choice == '3':
                    result_temp = input_temp + 273.15
                    print(f"Result: {input_temp} C = {result_temp:.2f} K")
                elif user_choice == '4':
                    result_temp = input_temp - 273.15
                    print(f"Result: {input_temp} K = {result_temp:.2f} C")
                elif user_choice == '5':
                    result_temp = (input_temp - 32) * 5/9 + 273.15
                    print(f"Result: {input_temp} F = {result_temp:.2f} K")
                elif user_choice == '6':
                    result_temp = (input_temp - 273.15) * 9/5 + 32
                    print(f"Result: {input_temp} K = {result_temp:.2f} F")
            
            except ValueError:
                print("Invalid input: Please enter a numeric value for the temperature.")
        else:
            print("Selection Error: Please choose a valid option (1-7).")

# Executing the application
if __name__ == "__main__":
    start_temperature_converter()
