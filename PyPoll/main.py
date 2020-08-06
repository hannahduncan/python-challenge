import os
import csv 

totalVotes = 0
name = ""
voteCount = 0
maxVoteCount = 0
votePercent = 0 
winner = 0 
voteList = []
candidatesList = []

csvPath = "Resources/election_data.csv"

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    next(csvReader,None)
    for row in csvReader:
        totalVotes = totalVotes + 1
        name = row[2]

        voteList.append(name)

        if name not in candidatesList:
            candidatesList.append(name)

print("Election Results\n")
print("---------------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("---------------------------------\n")

for value in candidatesList:
    voteCount = voteList.count(value)
    votePercent = voteCount/totalVotes * 100
    print(f"{value}: {votePercent}% ({voteCount})\n")

    if voteCount > maxVoteCount:
        maxVoteCount = voteCount
        winner = value

print("---------------------------------\n")        
print(f"Winner: {winner}\n")
print("---------------------------------\n") 

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