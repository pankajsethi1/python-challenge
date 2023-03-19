import os
import csv
import statistics

# Specify the file to read from
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialise the following to 0 to calculate 
monthcount = 0  # of months
total = 0  # Total profit/loss

# Initialise list to store changes in profit/loss every month
changes = []

months = []

#Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        monthcount = monthcount + 1  # Count # of rows
        rowamount = int(row[1])  # Covert profit/loss amputnt to int and store in rowamount
        total = total + rowamount  # Add profit/loss for each row  
        # Calculate change from 2nd month only
        if monthcount > 1:  
            change = rowamount - prevamount
            changes.append(change)
            months.append(row[0]) # Store months against the changes
        prevamount = rowamount  # Store the current month amount for calculating the change for next month 
  
average = round( statistics.mean(changes),2) #  Find the average change

#  Fnd the minimum and maximum changes and the corresponding months
maxchange = max(changes)
maxchangemonth = months[changes.index(maxchange)]
minchange = min(changes)
minchangemonth = months[changes.index(minchange)]

# Print the result
print ("Financial Analysis\n----------------------------\nTotal Months: "+ str(monthcount) +
        "\nTotal: $" + str(total) + "\nAverage Changes: $"+str(average) +"\nGreatest Increase in Profits: "+ maxchangemonth +
        " ($" + str(maxchange)+")\n" + "Greatest Decrease in Profits: " + minchangemonth +
        " ($" + str(minchange)+")")

 # Specify the file to write to
output_path = os.path.join("analysis", "financial_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change','Greatest Increase in Profits','Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([monthcount,"$" + str(total),"$" + str(average),maxchangemonth +
        " ($" + str(maxchange)+")",minchangemonth +" ($" + str(minchange)+")"])


 
