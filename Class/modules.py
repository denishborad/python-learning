# from Object import turism
class bus:

    seats = 45
    def __init__(self,name,age,member):
        self.name = name
        self.age = age
        self.member = member

    def get_Info(self):
        print("Hello, ",self.name)
        print("Denish Your age is: ",self.age)
        print("Your Femily Menber is :",self.member)

# turism.busname
b = bus("Denish",'21','4')
print(b.seats)
b.get_Info()
