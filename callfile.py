import csv 
f = open('csvfile.csv','r')
reader = csv.reader(f)

for row in reader:
    print(row)
