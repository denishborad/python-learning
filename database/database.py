import sqlite3

conn = sqlite3.connect("database.db")
print("opened database successfullly")

# conn.execute('''CREATE TABLE student
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             EMAIL TEXT NOT NULL);
#             ''')
# print("Table Created ")

# Insert statement

ID = input('ID:')
NAME = input('Name:')
EMAIL = input('EMAIL:')

conn.execute("INSERT INTO student (ID,NAME,EMAIL) \
    VALUES (?,?,?)",(ID,NAME,EMAIL))

    
# conn.execute("INSERT INTO student (ID,NAME,EMAIL) \
    # VALUES (2,'borad','borad@gmail.com')")

conn.commit()
print("Data Inserted")

# Update statement

# conn.execute("UPDATE student set NAME = 'DENISH' where ID = 1")
# conn.commit()
# print("Update Row :", conn.total_changes)

# Delete statement

# conn.execute("DELETE FROM student where ID = 2")
# conn.commit()
# print("Delete Row",conn.total_changes)

conn.close()