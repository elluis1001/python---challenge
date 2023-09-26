#Bring in the files for PyBank
import os

#module for reading CSV files
import csv

#declaring variables
Total_months = []
TotalOfProfitLoss = 0
PreviousProfitLoss = 0
ChangeInProfitLoss = 0
average_ChangeInProfitLoss = 0
ChangeInProfitLoss_list = []
Great_inc = ["", 0]
Great_dec = ["", 0]

#set the path to open files and csv files
csvpath = os.path.join("Resources", "budget_data.csv")

#set a path for creating text file with the results desired
analysis_file = os.path.join("analysis", "budget_analysis.txt")

#open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header
    csvreader = next(csvfile)

    rowcount = 0

    #loop through the data in the rows
    for row in csv.reader(csvfile):

        rowcount += 1
        #total of the profit/loss column
        TotalOfProfitLoss += int(row[1]) 
        
        #change in profit/loss within rows
        ChangeInProfitLoss = int(row[1]) - PreviousProfitLoss
        ChangeInProfitLoss_list.append(ChangeInProfitLoss)
        PreviousProfitLoss = int(row[1])

        # greatest inc and decrease
        if ChangeInProfitLoss > Great_inc[1]:
            Great_inc[0] = row[0]
            Great_inc[1] = ChangeInProfitLoss
        
        if ChangeInProfitLoss < Great_dec[1]:
            Great_dec[0] = row[0]
            Great_dec[1] = ChangeInProfitLoss

#average profit loss change
average_ChangeInProfitLoss = sum(ChangeInProfitLoss_list[1:]) / len(ChangeInProfitLoss_list[1:])



print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: ", rowcount)
print(f"Total: ${TotalOfProfitLoss}")
print(f"Average Change:  ${average_ChangeInProfitLoss:.2f}")
print(f"Greatest Increase in Profits: {Great_inc[0]} (${Great_inc[1]})")
print(f"Greatest Decrease in Profits: {Great_dec[0]} (${Great_dec[1]})")

#creating txt file
with open(analysis_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write("Total Months: 86\n")
    txtfile.write(f"Average Change:  ${average_ChangeInProfitLoss:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {Great_inc[0]} (${Great_inc[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Great_dec[0]} (${Great_dec[1]})\n")
#print
print(analysis_file)






