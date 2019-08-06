# Modules
import os
import csv

counter = 0
nettotal = 0

path = "budget_data.csv"

with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    # let's call the header:
    csv_header = next(csvfile)
    print(csv_header)

    for row in csvreader:
        print(row)
        nettotal = nettotal + int(row[1])
        counter = counter + 1


print(nettotal)
print(counter)
     


