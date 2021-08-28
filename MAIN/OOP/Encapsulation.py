 class SoftwareEngineer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None # _x mean protected variable __x mean private variable
        self.bug_fix=0

    def code(self):
        self.bug_fix += 1

#getter
    def get_salary(self):
        return self._salary
#setter
    def set_salary(self,base_salary):
        self._salary=self._calculate_salary(base_salary)

    def _calculate_salary(self,base_value):
        if(self.bug_fix<10):
            return base_value
        if(self.bug_fix<100):
            return base_value*2
        return base_value*3

se1=SoftwareEngineer("lal",22)
print(se1.age,se1.name,se1._salary)

se1.set_salary(6000)
print(se1.get_salary())

for i in range(10):
    se1.code()

se1.set_salary(5000) #Abtaction
print(se1.get_salary())