#inharit, extend, override

class Employe:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

    def work(self):
        print(f"{self.name} work...")

class SoftwareEnginner(Employe):
    def __init__(self,name,age,city,level): #override attribute
        super().__init__(name,age,city)
        self.level=level
    def coding(self):
        print(f"{self.name} is coding...")

    def work(self):
        print(f"{self.name} minning...") #override method

class Desiger(Employe):
    def drawing(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} edtiing...") #override method

e1=SoftwareEnginner('lal',65,'colombo','junior')
print(e1.level)
d1=Desiger("kl",44,"ttt")
print(d1.name)
e1.work()
d1.work()
e1.coding()
d1.drawing()