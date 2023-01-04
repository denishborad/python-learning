# import csv

# file = open("denish.csv")
# type(file)
# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# header

# rows = []
# for row in csvreader:
#         rows.append(row)
# rows

# import csv
# rows = []
# with open("denish.csv", 'r') as file:
#     csvreader = csv.DictReader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)


# with open('denish.csv') as f:
#     denish = csv.DictReader(f)
#     for deni in denish:
#         print(deni)


# with open("denish.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print((row))
file = open('denish.csv','r+')
file.write(str('denish'))
file.write('\n')

file.close()

#add new line

# writer = csv.writer(csvfile) 
# # Write the new line to the CSV file 
# writer.writerow(['value1', 'value2', 'value3'])