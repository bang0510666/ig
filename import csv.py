import csv

with open('names.csv', newline='') as csvfile:

  rows = csv.reader(csvfile)

  for row in rows:
    print(row)