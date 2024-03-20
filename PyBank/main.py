# Import Modules needed
import os
import csv

# Define variables for path definition
pathquestion = ""
directory = ""

# Loop to ask for current directory to define path
while pathquestion != "A" and pathquestion != "B":
    
    # Ask user their current location
    print("What directory are you executing main.py from?\n\
A. /../python-challenge\n\
B. /../python-challenge/PyBank\n\
Please enter A or B\n\
(If your current directory is none of these,\n\
enter EXIT and navigate to either one of the locations\n\
before executing main.py)")
    
    # User to input option about their current directory
    pathquestion = input()
    
    # If statement to define directory
    if pathquestion == "A":
        directory = "PyBank"
    elif pathquestion == "B":
        directory = ""
    elif pathquestion == "EXIT":
        exit()
    else:
        print ("Option not avaliable, please enter A, B or EXIT")

# Set the path for the csv file based on the answer
budgetpath = os.path.join(directory,"Resources","Budget_data.csv")

# Try to open the csv file and if error, indicate the choice was wrong and exit 
try:
    with open(budgetpath,'r') as budgetdata:
        budgetreader = csv.reader(budgetdata)
except:
    print("You chose the wrong option,\n\
please execute main.py again and select the right option")
    exit()

# Open the csv file 
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
    totalchanges = 0

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

# Analysis header
Line_1 =(f"Financial Analysis\n\n----------------------------")

# Total months          
Line_2 = (f"Total Months: {len(ProfitLosses)}")

# Total Profits/Losses
Line_3 = (f"Total: $ {totalPL}")

# Average changes
Line_4 = (f"Average Change: $ {round(averagechanges,2)}")

# Greatest Increase and its month
Line_5 = (f"Greatest Increase in Profits: {months[changes.index(max(changes))+1]} ($ {max(changes)})")

# Greatest Decrease and its month
Line_6 = (f"Greatest Decrease in Profits: {months[changes.index(min(changes))+1]} ($ {min(changes)})")

# Concatenate summmary
summary = (f"{Line_1}\n\n{Line_2}\n\n{Line_3}\n\n{Line_4}\n\n{Line_5}\n\n{Line_6}")

# Print summary in Terminal
print(summary)

# Define path for text file
analysispath = os.path.join(directory,"Analysis","Budget_analysis.txt")

# Create text file and open it on write mode
with open(analysispath,'w') as analysisfile:
    
    # Add information to the text file
    analysisfile.write(summary)