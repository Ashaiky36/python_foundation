#calculating sum of price column of a csv
import csv

with open(r'C:\Users\Ahad\Documents\Shopping.csv', 'r') as splist:
    next(splist)
    total = 0
    for row in csv.reader(splist):
        total += int(row[1])

print(total)   