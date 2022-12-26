from turism import turism1

class bus1:
    busname = "volvo"
    seats = 60
    driver = 2

    def __init__(self,busname,seats,driver):
        self.busname = busname
        self.seats = seats
        self.driver = driver

    def get_Info(self):
        print("Bus Name is : ",self.busname)
        print("Seats Are : ",self.seats) 
        print("Driver is : " ,self.driver)

p = bus1("volvo","60","2")
print(p.busname)
print(p.seats)
print(p.driver)
p.get_Info()




# turism1.turist
# turism1.place
# turism1.prise
# turism1.turismname