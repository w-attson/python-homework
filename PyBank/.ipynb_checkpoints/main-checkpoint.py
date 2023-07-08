import csv
import numpy as np
from pathlib import Path

# Path to collect data from the Resources folder
budget_data_path = Path("./budget_data.csv")

# Initialise budget records
budget_records = []
 
# Read in the CSV file
with open(budget_data_path, "r") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter = ",")
    
    # Read the header row
    budget_header = next(budget_reader)
    #print(budget_header)
       
    # Initialise variables
    total_months = 0
    total_revenue = 0
    previous_month = 0
    monthly_change = 0
    greatest_decrease = 0
    greatest_increase = 0
    delta_list = []
    
    # Read each row of data following header 
    for row in budget_reader:

        # Calculate the totals
        total_months += 1
        total_revenue += int(row[1])

        # Calculate the average change
        monthly_change = int(row[1]) - previous_month
        previous_month = int(row[1])
        delta_list += [monthly_change]
        
        # Calculate the greatest increase
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_month = row[0]
        
        # Calculate the greatest decrease
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_month = row[0]

average_delta = (np.mean(delta_list[1:]))
average_delta = round(average_delta,2)

# Print the calculations to the terminal
print()
print("Financial Analysis")
print()
print("-----------------------------------")
print()
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_delta}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
print()

# Output the calculations to the text file
output = Path("budget_data_completed.txt")

with open(output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_revenue}\n")
    file.write(f"Average Change: ${average_delta}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
    file.write("\n")