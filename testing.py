import csv

with open("names.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)