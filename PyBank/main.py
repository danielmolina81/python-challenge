
#Import Modules needed
import os
import csv

#Set the path for the csv file
csvpath = os.path.join("PyBank/Resources/budget_data.csv")

#Open the CSV 
with open(csvpath) as budgetdata:
    budgetreader = csv.reader(budgetdata, delimiter=',')
    
    #Extract header
    header = next(budgetreader)
    
    ProfitLosses = []
    totalPL = 0
    changes = []
    change = 0
    totalchanges=0

       # Loop through data
    for month in budgetreader:
        ProfitLosses.append(int(month[1]))

    for month in ProfitLosses:
        totalPL += month

    for month in range(1,len(ProfitLosses)):
        change = ProfitLosses[month] - ProfitLosses[month-1]
        changes.append(int(change))

    for change in changes:
        totalchanges += change
    
    averagechanges = totalchanges/len(changes)

print(
f"Financial Analysis\n\n\
----------------------------\n\n\
Total Months: {len(ProfitLosses)}\n\n\
Total: $ {totalPL}\n\n\
Average Change: $ {round(averagechanges,2)}\n\n\
Greatest Increase in Profits: Aug-16 ($ {max(changes)})\n\n\
Greatest Decrease in Profits: Feb-14 ($ {min(changes)})\n")
    
#Dim Total_Rows As Double
#Dim Total_Months As Double
#Dim Total As Double
#Dim Change As Double
#Dim Greatest_Increase_Month As Double
#Dim Greatest_Increase As Double
#Dim Greatest_Decrease_Month As Double
#Dim Greatest_Decrease As Double
#Dim Total_Change As Double
#Dim Average_Change As Double

# Total_Rows = Cells(Rows.Count, 1).End(xlUp).Row
# Total_Months = Total_Rows-1
# Total = cells(2,2).value

# for i = 3 to Total_Rows
#     Total = Total + Cells(i,2).value
#     Change = Cells(i,2).value-Cells(i-1,2).value
#         If Change>Greatest_Increase then
#             Greatest_Increase = Change
#             Greatest_Increase_Month = Cells(i,1).value
#         End if
#         If Change<Greatest_Decrease then
#             Greatest_Decrease = Change
#             Greatest_Decrease_Month = Cells(i,1).value
#         End if
#     Total_Change = Total_Change + Change

# Next i

# Average_Change = Total_Change/(Total_Months-1)

# Cells (2,5).value = Total_Months
# Cells(3,5).value= Total
# Cells(4,5).value = Average_Change
# Cells(5,4).value = Greatest_Increase_Month
# Cells(5,5).value = Greatest_Increase
# Cells(6,4).value = Greatest_Decrease_Month
# Cells(6,5).value = Greatest_Decrease
    