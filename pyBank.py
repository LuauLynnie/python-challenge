# Modules
import os
import csv

path = "budget_data.csv"

with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    # let's call the header:
    csv_header = next(csvfile)
    print(csv_header)

for row in csvreader:
    print(f"{row[0]} and {row[1 - 1]}")

# 1)Calculate number of months (rows except header)
for x in range(1, 100):
    print(x)


     


