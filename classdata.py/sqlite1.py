import csv
import sqlite3

conn = sqlite3.connect("sqlite1.db")
cursor = conn.cursor()
print("connected")

# conn.execute('''CREATE TABLE std
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#             NAME TEXT NOT NULL,
#             EMAIL TEXT NOT NULL);
#             ''')
# print("Table Created ")

class ddd:    
    def create():
        # id = input('id: ')
        # Name = input('name: ')
        # Email = input('email: ')
    
        # conn.execute("INSERT INTO std (Name,Email) VALUES(?, ?)",(Name,Email))
        # print("inserted")
        
        # conn.execute("UPDATE std set Email = 'DENISH@gmail.com' where ID = 3")
        # print("Update Row :", conn.total_changes)

        # conn.execute("DELETE FROM std where Id = ?")
        # print("Deteled",conn.total_changes)

        conn.commit()
        cursor.execute("select * from std")
        with open("sqlite1.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            # csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
            # csv_reader = csv.reader(csv_file)
            # for row in csv_reader:
                # print(row)
        conn.close()

    def rewrite():
        file = open('sqlite1.csv','r')
        reader=csv.reader(file)
        L=[]
        id=int(input("Enter Id : "))
        f=False
        for row in reader:
            if row[0]==str(id):
                f=True
            else:
                L.append(row)
        file.close()

        if f==False:
            print("Id Not Found!!!")
        else:
            file=open('sqlite1.csv','w+',newline='')
            writer=csv.writer(file)
            writer.writerow(L)

            reader = csv.reader(file)
            for row in reader:
                print(row)
            file.close()

s = ddd