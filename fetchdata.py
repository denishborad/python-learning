import sqlite3
import csv 

#Connecting to sqlite
conn = sqlite3.connect('database1.db')

cursor = conn.cursor()

file = open('fetchdata.csv','w+')
select_all = "SELECT * FROM student"

reader = cursor.execute(select_all).fetchall()
writer = csv.writer(file)

writer.writerow(reader)
content = csv.DictReader(file)

for row in reader:
    print(row)

conn.commit()

file.close()
conn.close()