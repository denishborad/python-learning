import csv
import sqlite3

# create database

conn = sqlite3.connect("user.db")
cursor = conn.cursor()
print("connected")

# conn.execute('''CREATE TABLE Usertable
# (ID INTEGER PRIMARY KEY AUTOINCREMENT,
# NAME TEXT,EMAIL TEXT,CITY TEXT);''')
# print("created table")

# open csv file

# with open("user.csv","r+") as file:
#     # create csv reader
#     reader = csv.reader(file)
#     # iterate over the row of the csv file 
#     i = 0
#     for row in reader:
#         # print values
#         print(row)
#         if i != 0:
#         # insert the row into the table
#             conn.execute("INSERT INTO Usertable (ID,NAME,EMAIL,CITY) VALUES (?,?,?,?)",row)
#         i = i+1
# # save the changes
conn.commit()

file = open('datafecth.csv','r+')
select_all = "SELECT * FROM Usertable"

reader = cursor.execute(select_all).fetchall()
writer = csv.writer(file)

writer.writerow(reader)
content = csv.DictReader(file)

for row in reader:
    print(row)

# close the connection
file.close()
conn.close()
