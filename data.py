# import csv
# import sqlite3
 
# # Connecting to the geeks database
# connection = sqlite3.connect('user.db')
 
# # Creating a cursor object to execute
# # SQL queries on a database table
# cursor = connection.cursor()
 
# # # Table Definition
# # create_table = '''CREATE TABLE person(
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 name TEXT NOT NULL,
# #                 email TEXT NOT NULL,
# #                 city TEXT NOT NULL);
# #                 '''
 
# # Creating the table into our
# # database
# # cursor.execute(create_table)
 
# # Opening the person-records.csv file
# file = open('user.csv')
 
# # Reading the contents of the
# # person-records.csv file
# contents = csv.reader(file)
 
# # SQL query to insert data into the
# # person table
# insert_records = "INSERT INTO person (id, name, email, city) VALUES(?, ?, ?, ?)"
 
# # Importing the contents of the file
# # into our person table
# cursor.executemany(insert_records, contents)
 
# # SQL query to retrieve all data from
# # the person table To verify that the
# # data of the csv file has been successfully
# # inserted into the table
# select_all = "SELECT * FROM person"
# rows = cursor.execute(select_all).fetchall()
 
# # Output to the console screen
# for r in rows:
#     print(r)
 
# # Committing the changes
# connection.commit()
 
# # closing the database connection
# connection.close()


import csv
import sqlite3

file = open('user.csv', 'r')
reader = csv.reader(file)

conn = sqlite3.connect('user.db')
cursor = conn.cursor()
print("connected")

# conn.execute('''CREATE TABLE Usertable
# (ID INTEGER PRIMARY KEY AUTOINCREMENT,
# NAME TEXT,EMAIL TEXT,CITY TEXT);''')
# print("created table")

for row in reader:
    print(row)

conn.execute("INSERT INTO Usertable (id,NAME,EMAIL,CITY) VALUES(?, ?, ?, ?)", row)

conn.commit()

conn.close()