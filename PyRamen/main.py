# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries

import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv

menu_filepath = Path('./menu_data.csv')
sales_filepath = Path('./sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data

menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, "r") as csvfile:
    menu_reader = csv.reader(csvfile, delimiter = ",")
    
    menu_header = next(menu_reader)
    
    for row in menu_reader:
        menu.append(row)


# @TODO: Read in the sales data into the sales list

with open(sales_filepath, "r") as csvfile:
    sales_reader = csv.reader(csvfile, delimiter = ",")

    sales_header = next(sales_reader)

    for row in sales_reader:
        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics

report = {}

# Initialize a row counter variable

row_count = 0

# @TODO: Loop over every row in the sales list object

for row in sales:

    # Line_Item_ID, Date, Credit_Card_Number, Quantity, Menu_Item
    # @TODO: Initialize sales data variables
    
    Line_Item_ID = row[0]
    Date = row[1]
    Credit_Card_Number = row[2]
    Quantity = int(row[3])
    Menu_Item = row[4]
    
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    
    sales_item = row[4]
    
    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}  

    # @TODO: For every row in our sales data, loop over the menu records to determine a match

    for row in menu:
        
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

        Item = row[0]
        Category = row[1]
        Description = row[2]
        Price = float(row[3])
        Cost = float(row[4])

        # @TODO: Calculate profit of each item in the menu data
        
        Profit = Price - Cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item

        if Menu_Item == Item:

            # @TODO: Print out matching menu data
            
            # @TODO: Cumulatively add up the metrics for each item key
            
            report[sales_item]["01-count"] += Quantity
            report[sales_item]["02-revenue"] += Price * Quantity
            report[sales_item]["03-cogs"] += Cost * Quantity
            report[sales_item]["04-profit"] += Profit * Quantity
            

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match

        else:
            sales_item != Item
            #print(f"{sales_item} does not equal {Item}! NO MATCH!")


    # @TODO: Increment the row counter by 1

    row_count += 1

# @TODO: Print total number of records in sales data

print(row_count)

# @TODO: Write out report to a text file (won't appear on the command line output)

output = Path("PyRamen - Report.txt")

with open(output, 'w') as file:
    file.write("PyRamen Report\n")
    file.write("-------------------------\n")
    file.write("SALES DATA\n")
    file.write("-------------------------\n")
    for row in report:
        file.write(f"{row},{report[row]}\n")
    file.write("-------------------------\n")
    file.write(f"Total number of records in sales data: {row_count}\n")
    file.write(f"Total number of records in menu data: {len(menu)}\n")
    file.write(f"Total number of records in report: {len(report)}\n")

