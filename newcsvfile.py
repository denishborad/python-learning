import csv

file = open('csvfile.csv','r+')
print('\n')
writer = csv.writer(file)
writer.writerow([int(input('sr no: ')),input('Name: '),input('Email: '),int(input('phone no: '))])
reader = csv.DictReader(file)
for row in reader:
    print(dict(row))
print(writer)
file.close()
