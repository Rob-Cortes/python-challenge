# Modules
import csv
import os

# Set path for file
csv_path = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)

    # List to store months
    months = []

    # List to store monthly profit/loss
    monthly_profit = []

    # Loop through the rows of the csv
    for row in csvreader:
        if not row[0] == "Date":
            months.append(row[0])
            monthly_profit.append(int(row[1]))

# Count months
month_count = len(months)

# Variable to compute total profit/loss
total_profit = 0

# List to store changes in monthly profit
delta_profit = []

# Variables to store max/min changes in monthly profit, and their corresponding months
max_delta = 0
max_delta_month = ''
min_delta = 0
min_delta_month = ''

# From Python class #3 materials, 07-Stu_Functions
# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# For loop with number of iterations = number of months
for x in range(month_count):

    # Increase total profit by the amount of monthly profit
    total_profit += monthly_profit[x]

    # Conditional to exclude first month from computation of change in profit
    if x > 0:

        # Compute change in monthly profit
        delta = monthly_profit[x] - monthly_profit[x-1]

        # Add change in monthly profit to list
        delta_profit.append(delta)

        # Conditional to capture changes that exceed prior max or min
        if delta > max_delta:
            max_delta = delta
            max_delta_month = months[x]
        elif delta < min_delta:
            min_delta = delta
            min_delta_month = months[x]

# Call previously defined function to compute average change in monthly profit 
avg_delta = average(delta_profit)

# Convert results to strings
str1 = "Financial Analysis"
str2 = "----------------------------------------------------------------"
str3 = f"Number of Months: {month_count}"
str4 = f"Cumulative Profit: ${total_profit}"
str5 = f"Average Change in Monthly Profit: ${avg_delta:.2f}"
str6 = f"Greatest Monthly Increase in Profit: {max_delta_month} (${max_delta})"
str7 = f"Greatest Monthly Decrease in Profit: {min_delta_month} (${min_delta})"

# Store results as a list of strings
results = [str1, str2, str3, str4, str5, str6, str7]

# Print results to the terminal
for line in results:
    print(line)

# Set path for results text file
results_path = os.path.join("analysis", "financial_results.txt")

# Store results in text file
with open(results_path, 'w') as f:
    for line in results:
        f.write(line)
        f.write('\n')
        

