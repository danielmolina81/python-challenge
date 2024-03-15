# Import Modules needed
import os
import csv

# Set the path for the csv file
budgetpath = os.path.join("PyBank/Resources/budget_data.csv")

# Open the CSV 
with open(budgetpath,'r') as budgetdata:
    budgetreader = csv.reader(budgetdata)
    
    # Extract header
    header = next(budgetreader)
    
    # Define Lists and Variables
    ProfitLosses = []
    months = []
    totalPL = 0
    changes = []
    change = 0
    totalchanges=0

    # Loop through data to obtain a list of profits and losses and a list of months
    for month in budgetreader:
        ProfitLosses.append(int(month[1]))
        months.append((month[0]))

    # Loop through the list of profits and losses to obtain the total Profits/Losses
    for month in ProfitLosses:
        totalPL += month

    # Loop through the list of profits and losses to calculate the changes month by month
    for month in range(1,len(ProfitLosses)):
        change = ProfitLosses[month] - ProfitLosses[month-1]

        # Create a list with the changes
        changes.append(int(change))
    
    # Loop through the list of changes to calculate the total changes
    for change in changes:
        totalchanges += change
    
    # Calculate the average of the changes
    averagechanges = totalchanges/len(changes)

# Print the analysis header on Terminal
print(f"Financial Analysis\n\n\----------------------------\n")

# Print Total months          
print(f"Total Months: {len(ProfitLosses)}\n")

# Print Total Profits/Losses
print(f"Total: $ {totalPL}\n")

# Print Average changes
print(f"Average Change: $ {round(averagechanges,2)}\n")

# Print Greatest Increase
print(f"Greatest Increase in Profits: Aug-16 ($ {max(changes)})\n")

# Print Greatest Decrease
print(f"Greatest Decrease in Profits: Feb-14 ($ {min(changes)})\n")

analysispath = os.path.join("PyBank/Analysis/Analysis.txt")