import os
import csv
import statistics

# Specify the file to read from
csvpath = os.path.join("Resources", "election_data.csv")

# Initialise the following to 0 to calculate 
votecount = 0  # Total votes

# initialise dictionary for candidatess 
candidates  = {}

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        votecount = votecount + 1  # Count # of rows
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1  # Add the votecounht if candidate exists in the dictionary
        else:

            candidates[row[2]] = 1  # Add the candidate to the dictionary with votecount 1

# Identify winning candidate
wincand = max(zip(candidates.values(), candidates.keys()))[1]

# Create the result
output = ("Election Results\n-------------------------\nTotal Votes: "+str(votecount)+"\n-------------------------\n")
for candidate in candidates:
    candvotecount = candidates[candidate]
    output=output+(candidate+": "+str(round(candvotecount/votecount*100,3))+"% ("+ str(candvotecount)+")\n")
output=output+("-------------------------\nWinner: "+wincand+"\n-------------------------")

# Print the result

print (output)

 # Specify the file to write to
output_path = os.path.join("analysis", "poll_analysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w') as file:

    # Write the results to the txt file
    file.write(output)



 
