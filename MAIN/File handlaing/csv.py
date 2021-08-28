import csv

with open('file.csv','a') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    rows = list(reader)
    for row in rows:
        print(', '.join(row))