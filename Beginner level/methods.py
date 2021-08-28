class Vehicle:
    gg="kl"
    def __init__(self,type,name):
        self.name=name
        self.type=type

    def brake(self):
        return "break",self.name,self.gg
    @classmethod
    def runinning(cls):
        return "running",cls.gg
    @staticmethod
    def overtaking():
        return "overtaking"

v1=Vehicle("hh","gdf")
print(v1.name,v1.type)
print(v1.runinning())
print(v1.overtaking())
print(Vehicle.overtaking())
print(v1.brake())
