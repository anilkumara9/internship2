# Statistical Sum and Average Calculator
# This program calculates the sum, average, maximum, and minimum values of a user-provided list.

try:
    # Determining how many data points to process
    data_points_count = int(input("How many numbers would you like to analyze?: "))
    
    if data_points_count <= 0:
        print("Error: Please provide a positive number of data points.")
    else:
        number_collection = []

        # Collecting numerical data from user
        for i in range(1, data_points_count + 1):
            while True:
                try:
                    entry_value = float(input(f"Enter value {i}: "))
                    number_collection.append(entry_value)
                    break
                except ValueError:
                    print("Invalid input detected. Please enter a numerical value.")

        # Calculating mathematical statistics
        total_aggregate_sum = sum(number_collection)
        calculated_average = total_aggregate_sum / data_points_count
        highest_value = max(number_collection)
        lowest_value = min(number_collection)
        
        # Displaying the statistical summary report
        print("\n--- DATA ANALYSIS SUMMARY ---")
        print(f"Numbers Processed: {data_points_count}")
        print(f"Total Sum        : {total_aggregate_sum:,.2f}")
        print(f"Mean (Average)   : {calculated_average:,.2f}")
        print(f"Highest Value    : {highest_value:,.2f}")
        print(f"Lowest Value     : {lowest_value:,.2f}")

except ValueError:
    print("Configuration Error: Please enter an integer for the count.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
