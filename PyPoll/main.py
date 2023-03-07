# Import modules
import os
import csv

# Path for csv source data
csv_path = os.path.join("Resources", "election_data.csv")

# Open csv source data
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)

    # Skip headers
    header = next(csvfile)

    # Declare dictionary of candidate names and vote counts
    candidates = {}

    # Loop through csv
    for row in reader:

        # If candidate name doesn't already exist in the dictionary...
        if not row[2] in candidates.keys():

            # ...add name and 1 vote to the dictionary
            candidates.update({row[2]: 1})
        
        # If candidate name already exists in the dictionary...
        else:

            # ...add 1 to the value of the corresponding key  
            candidates[row[2]] = candidates[row[2]] + 1

# Declare total vote count variable 
total_votes = 0

# Loop through values in candidates dictionary
for votes_received in candidates.values():

    # Increase total vote count by the values
    total_votes += votes_received

# Separator string for easier reading of printed results
separator = "------------------------------"

# Initialize list of strings for results, including the title of the analysis, separators, and total vote count 
results = ["Election Results", separator, f"Total Votes: {total_votes}", separator]

# Initialize variables for winning percentage of vote and winner's name  
winning_pct = 0
winning_name = ""

# Loop through keys and values in candidates dictionary
for x, y in candidates.items():

    # For each candidate, compute percentage of total votes received
    pct = (y / total_votes) * 100

    # Create string to display results for each candidate
    newstr = f"{x}: {pct:.3f}% ({y})"

    # Append string to results string-list
    results.append(newstr)

    # Conditional to determine winning candidate
    if pct > winning_pct:
        winning_pct = pct
        winning_name = x

# Append more separators, and winner result to the results string-list
results.append(separator)
results.append(f"Winner: {winning_name}")
results.append(separator)

# Print results to the terminal
for line in results:
    print(line)

# Set path for results text file
results_path = os.path.join("analysis", "election_results.txt")

# Store results in text file
with open(results_path, 'w') as f:
    for line in results:
        f.write(line)
        f.write('\n')