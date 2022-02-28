import os
import csv

#set csv file path
csvpath = os.path.join("Resources", "budget_data.csv")

#variables
monthtotal = 0
totalpl = 0
pl = []
month = []
monthlychange = []

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvheader = next(csvreader)
        for row in csvreader:
            monthtotal = monthtotal + 1
            totalpl = totalpl + int(row[1])
            pl.append(row[1])
            month.append(row[0])

firstmonthpl = int(pl[0])

#loop monthly change in profit
for i in range(1, len(pl)):
    monthlychange.append(int(pl[i]) - firstmonthpl)
    firstmonthpl = int(pl[i])
    i = i + 1

#Average Change
averagechange = sum(monthlychange) / len(monthlychange)
averagechange = round(averagechange, 2)

#Greatest Increase/Decrease In Profts
maxmonthlychange = max(monthlychange)
minmonthlychange = min(monthlychange)

#MaxMinMonth
maximonth = monthlychange.index(max(monthlychange)) + 1
minimonth = monthlychange.index(min(monthlychange)) + 1

#financial analysis terminal ouput
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {monthtotal}')
print(f'Total: ${totalpl}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {month[maximonth]} (${maxmonthlychange})')
print(f'Greatest Decrease in Profits: {month[minimonth]} (${minmonthlychange})')

#textfile output
textoutput = os.path.join("PyBank.txt")

with open(textoutput, "w") as textfile:
    textfile.write('Financial Analysis')
    textfile.write("\n")
    textfile.write('----------------------------')
    textfile.write("\n")
    textfile.write(f'Total Months: {monthtotal}')
    textfile.write("\n")
    textfile.write(f'Total: ${totalpl}')
    textfile.write("\n")
    textfile.write(f'Average Change: ${averagechange}')
    textfile.write("\n")
    textfile.write(f'Greatest Increase in Profits: {month[maximonth]} (${maxmonthlychange})')
    textfile.write("\n")
    textfile.write(f'Greatest Decrease in Profits: {month[minimonth]} (${minmonthlychange})')

