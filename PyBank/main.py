import csv

# Path to collect data from the Resources folder

file = open("budget_data.csv", "r")
budget_data = list(csv.reader(file, delimiter = ","))
file.close()

print(budget_data)

# Initiate Variables

total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greastest_decrease = 0


'''
budget_data = []

# Initiate Variables

total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greastest_decrease = 0

# Open CSV File




for date, profit_loss in budget_data.items():
    print(date, profit_loss)
    


# Totals

for accounts in budget_data:
    
    total_months += 1
    total += accounts
    
    print(total_months)
    print(total)
    

print()
print("Financial Analysis")
print()
print("-----------------------------------")
print(f"Total Months: {}")
print(f"Total: ${}")
print(f"Average Change: {}")
print(f"Greatest Increase in Profits: {}")
print(f"Greatect Decrease in Profits: {}")
print()

'''