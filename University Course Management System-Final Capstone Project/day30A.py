#adding values from a list of dictonaries into a csv
import csv
Data = [{"name" : "Ahad", "email" : "ahad@email.com", "age" : 21},
        {"name" : "John", "email" : "john@email.com", "age" : 37},
        {"name" : "Chloe", "email" : "ch@email.com", "age" : 20}]

with open(r'C:\Users\Ahad\Documents\Book1.csv', 'w', newline= '') as csvfile:
    fieldnames = ["name", "email", "age"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(Data)

 

