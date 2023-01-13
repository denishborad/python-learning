import sqlite3

conn = sqlite3.connect("database1.db")
print("opened database successfullly")

# conn.execute('''CREATE TABLE student
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#             NAME TEXT NOT NULL,
#             EMAIL TEXT NOT NULL);
#             ''')
# print("Table Created ")

# Insert statement

NAME = input('Name:')
EMAIL = input('EMAIL:')

conn.execute("INSERT INTO student (NAME,EMAIL) \
    VALUES (?,?)",(NAME,EMAIL))

conn.commit()
print("Data Inserted")

conn.close()
