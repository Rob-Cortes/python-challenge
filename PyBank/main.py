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
            monthly_profit.append(row[1])

# Count months
month_count = len(months)

# Variable to compute total profit/loss
total_profit = 0

# Loop through monthly profit
for x in monthly_profit:
    total_profit = total_profit + x


        

