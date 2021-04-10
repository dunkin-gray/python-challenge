#import modules
import os
import csv

#set local pc path to data csv file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#set totalAmount variable
months = []
amounts = []
change = []
changeMonth = []

count = 0

#open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header = next(csvfile)

    #read through each row of data after the header
    for row in csv.reader(csvfile):

        #first time through set the newAmount for calculation
        if count == 0:
            #add 1 for first pass only
            count = count + 1
            #set amount for future calculations
            newAmount = int(row[1])
            #add amounts to amount list
            amounts.append(int(row[1]))
            #add months to month list
            months.append(str(row[0]))
        else:
            #add amounts to amount list
            amounts.append(int(row[1]))
            #add months to month list
            months.append(str(row[0]))
            #calculate change
            change.append(int(int(row[1]) - newAmount))
            #append change month
            changeMonth.append(str(row[0]))
            #set new amount for next row
            newAmount = int(row[1])

    #calculate results based on for loop entries
    totalMonths = len(months)
    totalAmount = sum(amounts)
    averageChange = round(sum(change) / len(changeMonth), 2)
    maxChange = max(change)
    maxChangeMonthIndex = change.index(maxChange)
    minChange = min(change)
    minChangeMonthIndex = change.index(minChange)

#print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: {totalAmount}')
print(f'Average Change: {averageChange}')
print(f'Greatest Increase in Profits: {changeMonth[int(maxChangeMonthIndex)]} ({maxChange})')
print(f'Greatest Decrease in Profits: {changeMonth[int(minChangeMonthIndex)]} ({minChange})')

#output the same results to a text file
output_path = os.path.join("..", "analysis", "financialAnalysis.txt")
with open(output_path, "w", newline='') as datafile:
    print('Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {totalMonths}\n'
    f'Total: {totalAmount}\n'
    f'Average Change: {averageChange}\n'
    f'Greatest Increase in Profits: {changeMonth[int(maxChangeMonthIndex)]} ({maxChange})\n'
    f'Greatest Decrease in Profits: {changeMonth[int(minChangeMonthIndex)]} ({minChange})', file=datafile)