# Import Modules needed
import os
import csv

# Set the path for the csv file
pollpath = os.path.join(".","PyPoll","Resources", "election_data.csv")

# Open the csv file 
with open(pollpath,'r') as polldata:
    pollreader = csv.reader(polldata)
    
    # Extract header
    header = next(pollreader)

    # Define Lists and Variables
    votes = []
    candidates = []
    countvotes = 0
    totalvotes = 0
    votescandidate = []
    percentcandidate = []
    results = []

    # Loop through data to obtain a list of all the votes
    for vote in pollreader:
        votes.append((vote[2]))

    totalvotes = len(votes)
    
    # Extract the list of unique candidates in alphabetical order
    candidates = sorted(set(votes))

    # Loop for each unique candidate to determine their amount of votes and their percentage
    for candidate in candidates:
        for vote in votes:
            if vote == candidate:
               countvotes += 1 
        votescandidate.append(countvotes)
        percentcandidate.append(round((countvotes/totalvotes)*100,3))
        countvotes = 0

    # Analysis header
    Line_1 = (f"Election Results")

    # Total votes          
    Line_2 = (f"Total Votes: {totalvotes}")

    # Loop to create a list with the results per candidate
    for candidate in candidates:
        results.append(f"{candidate}: {percentcandidate[candidates.index(candidate)]}% ({votescandidate[candidates.index(candidate)]})")

    # Result per candidate
    Line_3='\n\n'.join(results)

    # Winner
    Line_4 = (f"Winner: {candidates[votescandidate.index(max(votescandidate))]}")

    # Line
    Line_X = (f"----------------------------")

    # Concatenate summmary
    summary = (f"{Line_1}\n\n{Line_X}\n\n{Line_2}\n\n{Line_X}\n\n{Line_3}\n\n{Line_X}\n\n{Line_4}\n\n{Line_X}")

    # Print summary in Terminal
    print(summary)

# Define path for text file
analysispath = os.path.join(".","PyPoll","Analysis", "Poll_analysis.txt")

# Create text file and open it on write mode
with open(analysispath,'w') as analysisfile:
        
        # Add information to the text file
        analysisfile.write(summary)