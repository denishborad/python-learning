file = open('datafecth.csv','r+')
select_all = "SELECT * FROM Usertable"

reader = cursor.execute(select_all).fetchall()
writer = csv.writer(file)

writer.writerow(reader)
content = csv.DictReader(file)

for row in reader:
    print(row)