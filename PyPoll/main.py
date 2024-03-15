# Import Modules needed
import os
import csv

# Set the path for the csv file
pollpath = os.path.join(".","PyPoll","Resources", "election_data.csv")

# Open the CSV 
with open(pollpath,'r') as polldata:
    pollreader = csv.reader(polldata)
    
    # Extract header
    header = next(pollreader)
    print(header)



# # Define path for text file
# analysispath = os.path.join(".","PyPoll","Analysis", "Poll_analysis.txt")

# # Create text file and open it on write mode
# with open(analysispath,'w') as analysisfile:
        
#         #add information to the file
#         analysisfile.write(summary)