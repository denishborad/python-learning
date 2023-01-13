import csv

class csvfile:
    conn = sqlite3.connect("comma.db")
    cursor = conn.cursor()
    print("Connected")

    

    file = open("Commaseparate.csv","r+")
    print("\n")
    writer = csv.writer(file)
    writer.writerow([int(input('sr no: ')),input('Name: '),input('Email: '),int(input('phone no: '))])
    reader = csv.reader(file)
    for row in reader:
        print((row))

    def get_data(file):
        print(file)

data = csvfile