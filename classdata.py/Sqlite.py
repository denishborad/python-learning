import sqlite3

conn = sqlite3.connect("sqlite1.db")
print("opened database successfullly")

# conn.execute('''CREATE TABLE std
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#             NAME TEXT NOT NULL,
#             EMAIL TEXT NOT NULL);
#             ''')
# print("Table Created ")

# Insert statement

NAME = input('Name:')
EMAIL = input('EMAIL:')

conn.execute("INSERT INTO std (NAME,EMAIL) \
    VALUES (?,?)",(NAME,EMAIL))
print("Data Inserted")

# Update statement

# conn.execute("UPDATE std set NAME = 'DENISH' where ID = 1")
# conn.commit()
# print("Update Row :", conn.total_changes)

# Delete statement

# conn.execute("DELETE FROM std where ID = 2")
# conn.commit()
# print("Delete Row",conn.total_changes)


conn.commit()

conn.close()
