import os
import csv

cvspath = os.path.join("bank.csv")


monthCount =0
net = 0
prevProfit =0 
changeProfit = 0
maxChange = 0
minChange =0 
changeArray = []
#totalChange = 0
maxMonth = ""
minMonth = ""


with open(cvspath) as csvFile:
    csvReader = csv.reader(csvFile,delimiter=",")
    
    next(csvReader, None)
    for row in csvReader:
        monthCount = monthCount + 1
        net = net + int(row[1])
        currentProfit = int(row[1])
        
        changeProfit = currentProfit - prevProfit

        if (changeProfit > maxChange):
            maxChange = changeProfit
            maxMonth = row[0]
        if (changeProfit < minChange):
            minChange = changeProfit
            minMonth = row[0]
        
        prevProfit = int(row[1])
        changeArray.append(changeProfit)
        #totalChange = totalChange + changeProfit
  
#avg = totalChange/monthCount
avg = sum(changeArray)/len(changeArray)

print("-------------------------------\n")
print(f"Total months: {monthCount}\n")
print(f"Total: {net}\n")
print(f"Average Change: {avg}\n")
print(f"Greatest Increase in Profits: {maxMonth} {maxChange}\n")
print(f"Greatest Decrease in Profits: {minMonth} {minChange}\n")


pyBankPath = "analysis.txt"
with open(pyBankPath,'w') as pyBank:
    pyBank.write("Financial Analysis\n")
    pyBank.write("-------------------------------\n")
    pyBank.write(f"Total months: {monthCount}\n")
    pyBank.write(f"Total: {net}\n")
    pyBank.write(f"Average Change: {avg}\n")
    pyBank.write(f"Greatest Increase in Profits: {maxMonth} {maxChange}\n")
    pyBank.write(f"Greatest Decrease in Profits: {minMonth} {minChange}\n")
