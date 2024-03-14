
#Import Modules needed
import os
import csv

#Set the path for the csv file
csvpath = os.path.join("PyBank","Resources", "budget_data.csv")

#csvpath = "Resources/budget_data.csv"

with open(csvpath) as budgetdata:

    budgetdatareader = csv.reader(budgetdata, delimiter=',')

    print(budgetdatareader)

    csv_header = next(budgetdatareader)
    
    print(f"CSV Header: {csv_header}")

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
    