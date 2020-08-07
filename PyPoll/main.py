#Import Dependencies
import os
import csv 

#Initialize variables
totalVotes = 0
name = ""
voteCount = 0
maxVoteCount = 0
votePercent = 0 
winner = ""
voteList = []
candidatesList = []

#Path for CSV 
csvPath = os.path.join("Resources/election_data.csv")

#Open and read election data
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Store header
    next(csvReader,None)
    #Loop through CSV to calculate total votes
    for row in csvReader:
        totalVotes = totalVotes + 1
        name = row[2]

        #Add each person voted for to voteList
        voteList.append(name)

        #Add new candidates to candidatesList
        if name not in candidatesList:
            candidatesList.append(name)

#Print results to terminal
print("Election Results\n")
print("---------------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("---------------------------------\n")

#Determine vote counts and percent for each candidate in candidatesList
for value in candidatesList:
    voteCount = voteList.count(value)
    votePercent = voteCount/totalVotes * 100
    print(f"{value}: {votePercent}% ({voteCount})\n")

    #Determine winner
    if voteCount > maxVoteCount:
        maxVoteCount = voteCount
        winner = value

print("---------------------------------\n")        
print(f"Winner: {winner}\n")
print("---------------------------------\n") 


#Open and write results to text file
pyPollPath = "Analysis/analysis.txt"
with open(pyPollPath,'w') as pyPoll:
    pyPoll.write("Election Results\n")
    pyPoll.write("---------------------------------\n")
    pyPoll.write(f"Total Votes: {totalVotes}\n")
    pyPoll.write("---------------------------------\n")

    for value in candidatesList:
        voteCount = voteList.count(value)
        votePercent = voteCount/totalVotes * 100
        pyPoll.write(f"{value}: {votePercent}% ({voteCount})\n")

        if voteCount > maxVoteCount:
            maxVoteCount = voteCount
            winner = value

    pyPoll.write("---------------------------------\n")        
    pyPoll.write(f"Winner: {winner}\n")
    pyPoll.write("---------------------------------\n") 