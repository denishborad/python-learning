# from bus import bus1

# class turism1:
#     turismname = "Travelers"
#     turist = 45
#     place = 5
#     prise = 6000

#     def __init__(self,turismname,prise):
#         self.turistname = turismname
#         self.prise = prise

#     def fun(self):
#         print("Turist Are : ",self.turismname)
#         print("Prise : ",self.prise)

# travel = turism1("travels",'5000')
# print(travel.turismname)
# print(travel.turist)
# print(travel.place)
# print(travel.prise)
# travel.fun()
# print(travel.fun())

# bus1.busname
# bus1.seats
# bus1.driver




class tour:
    bus = 2
    turist = 60

    def __init__(self,bus,turist):
        self.bus = bus
        self.turist = turist
    def fun(self):
        print("Bus Number:",self.bus)
        print("Turist Number:",self.turist)

t = tour(2,60)
print(t.bus)
print(t.turist)
t.fun()