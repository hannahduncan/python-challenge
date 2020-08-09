#Import Dependencies
import os
import csv

#Path to CSV
cvspath = os.path.join("Resources/bank.csv")

#Initialize variables
monthCount =0
net = 0
prevProfit =0 
changeProfit = 0
maxChange = 0
minChange =0 
changeArray = []
header = []
firstRow = ""
maxMonth = ""
minMonth = ""

#Open and read CSV
with open(cvspath) as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")

    #Store header and record info from first row of data
    header = next(csvReader, None)
    firstRow = next(csvReader)
    monthCount = monthCount + 1
    net = net + int(firstRow[1])
    prevProfit = int(firstRow[1])
    
    #Loop through rows in CSV to compute analytics
    for row in csvReader:
        monthCount = monthCount + 1
        net = net + int(row[1])
        currentProfit = int(row[1])
        
        changeProfit = currentProfit - prevProfit
        prevProfit = int(row[1])
        changeArray.append(changeProfit)

        if (changeProfit > maxChange):
            maxChange = changeProfit
            maxMonth = row[0]
        if (changeProfit < minChange):
            minChange = changeProfit
            minMonth = row[0]

#Compute average change
avg = round(sum(changeArray)/len(changeArray),2)

#Print results to terminal
print("Financial Analysis\n")
print("-------------------------------\n")
print(f"Total months: {monthCount}\n")
print(f"Total: ${net}\n")
print(f"Average Change: ${avg}\n")
print(f"Greatest Increase in Profits: {maxMonth} (${maxChange})\n")
print(f"Greatest Decrease in Profits: {minMonth} (${minChange})\n")

#Open and write results to text file
pyBankPath = "Analysis/analysis.txt"
with open(pyBankPath,'w') as pyBank:
    pyBank.write("Financial Analysis\n")
    pyBank.write("-------------------------------\n")
    pyBank.write(f"Total months: {monthCount}\n")
    pyBank.write(f"Total: ${net}\n")
    pyBank.write(f"Average Change: ${avg}\n")
    pyBank.write(f"Greatest Increase in Profits: {maxMonth} (${maxChange})\n")
    pyBank.write(f"Greatest Decrease in Profits: {minMonth} (${minChange})\n")

