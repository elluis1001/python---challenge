#bring in files 
import os

import csv

#establishing path
csvpath = os.path.join("ResourcesPyPoll", "election_data.csv")

#path for printing text to txt.file 'style'
pypoll_analysis_file = os.path.join("analysisPyPoll", "analysisPyPoll.txt")

# Variables
TotalVotes = 0
Candidates = set()
CandVotes = {}

# Read the CSV file
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    
    # Move to next row
    next(reader)
    
    # filtering through each row for candidates and setting up variables
    for row in reader:
        TotalVotes += 1
        #column candidate names
        Candidate = row[2]
        Candidates.add(Candidate)
        # grabbing candidate vote counts and information
        CandVotes[Candidate] = CandVotes.get(Candidate, 0) + 1

# Calculate the percentage of votes each candidate won
VotePer = {candidate: (votes / TotalVotes) * 100 for candidate, votes in CandVotes.items()}

# Winner, Winner!!
Win = max(CandVotes, key = CandVotes.get)

# Print the results
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------------------------")
for Candidate in Candidates:
    print(f"{Candidate}: {VotePer[Candidate]:.3f}% ({CandVotes[Candidate]})")
print("----------------------------------------")
print(f"Winner: {Win}")
print("----------------------------------------")

#writing and printing the text file to 'analysisPyPoll'
with open(pypoll_analysis_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Votes: {TotalVotes}\n")
    txtfile.write("------------------------------------\n")
    for Candidate in Candidates:
        txtfile.write(f"{Candidate}: {VotePer[Candidate]:.3f}% ({CandVotes[Candidate]})\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Winner: {Win}\n")
    txtfile.write("------------------------------------\n")

#print the txtfile:
print(pypoll_analysis_file)



        
        







