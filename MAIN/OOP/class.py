class person:
    #class attributes
    count=0
    #constructor
    def __init__(self,name,age,height):
        #inctence attributes
        self.name=name
        self.age=age
        self.height=height
        person.count+=1
    # def __del__(self):
    #     print("object deleted")

    #one of deunder method
    def __str__(self):
        return "name: {}, age: {}, height: {}".format(self.name,self.age,self.height)

    def __eq__(self, other):
        return self.name==other.name

    #instance method
    def work(self):
        print(f"{self.name}:coding>>>")


    @staticmethod #decarator
    def salary(experience):
        if experience>2:
            print("5666")
        else:
            print("7000")



#instance
person1=person("lal",67,66)
person2=person("lal",67,66)
person3=person("wal",55,33)
print(person1.name)
print(person1.age)
print(person1.height)
print(person1)
print(person.count)
person1.work()
# del person1 #delete the object

print(person1==person2)
person1.salary(44)

