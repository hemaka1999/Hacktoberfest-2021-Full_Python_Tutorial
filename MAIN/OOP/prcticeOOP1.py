class Vehicle:
    colour="white"
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def seating_capacity(self, capacity):
        self.capacity=capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)


    def fare(self):
        return self.capacity * 100*(11/10)




vehicle1=Vehicle("lal",100,120)
bus1=Bus('TATA',120,20000)
print(bus1.seating_capacity(50))
print(vehicle1.max_speed)
print(vehicle1.mileage)
print(bus1.fare())
print(f'name:{bus1.name} speed:{bus1.max_speed} and colur is {Vehicle.colour}')
print(type(bus1))
print(isinstance(bus1,Vehicle))