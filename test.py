import csv

f = open('users.csv')
csv_f = csv.reader(f)
print(type(csv_f))

