# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
netprofit = None
increasepreviousprofit = None
decreasepreviousprofit = None
greatestincrease = 0
greatestincreasedate = ''
greatestdecrease = 0
greatestdecreasedate = ''

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    
    # Extract first row to avoid appending to net_change_list
    for row in reader:
        
        
        # Track the total and net change
        

        # Process each row of data
        #for row in reader:
        date = row[0]
        #for row in reader:
        profitloss = int(row[1])

        # Track the total
        total_months += 1
        total_net += profitloss
       
        # Track the net change
        if netprofit is not None:
            change = profitloss - netprofit
            net_change_list.append(change)

        netprofit = profitloss
        
        

        # Calculate the greatest increase in profits (month and amount)
        increasedate = row[0]
        increaseprofitchange = int(row[1])

        if increasepreviousprofit is not None:
            increasechange = increaseprofitchange - increasepreviousprofit
            if increasechange > greatestincrease:
                greatestincrease = increasechange
                greatestincreasedate = increasedate

        increasepreviousprofit = increaseprofitchange

        # Calculate the greatest decrease in losses (month and amount)
        decreasedate = row[0]
        decreaseprofitchange = int(row[1])

        if decreasepreviousprofit is not None:
            decreasechange = decreaseprofitchange - decreasepreviousprofit
            if decreasechange < greatestdecrease:
                greatestdecrease = decreasechange
                greatestdecreasedate = decreasedate
        
        decreasepreviousprofit = decreaseprofitchange

        



# Calculate the average net change across the months
if net_change_list:
    averagenetchange = sum(net_change_list) / len(net_change_list)
else:
    averagenetchange = 0

averagenetchange = round(averagenetchange,2)

# Generate the output summary
Title = "Financial Analysis\n"
titlebreak = "----------------------------\n"
totalmonthoutput = f'Total Months: {total_months}\n'
totalnetoutput = f'Total: ${total_net}\n'
averageoutput = f'Average Change: ${averagenetchange}\n'
greatestincreaseoutput = f'Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})\n'
greatestdecreaseoutput = f'Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})\n'


# Print the output
print(Title)
print(titlebreak)
print(totalmonthoutput)
print(totalnetoutput)
print(averageoutput)
print(greatestincreaseoutput)
print(greatestdecreaseoutput)
#print(net_change_list)



# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(Title)
    txt_file.write(titlebreak)
    txt_file.write(totalmonthoutput)
    txt_file.write(totalnetoutput)
    txt_file.write(averageoutput)
    txt_file.write(greatestincreaseoutput)
    txt_file.write(greatestdecreaseoutput)

