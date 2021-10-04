class Singleton:
    
   __instance = None
   id = 0

   @staticmethod 
   def getInstance():
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

   def incrementID(self):
      self.id += 1
   
   def getID(self):
      return self.id

s = Singleton()

print( "ID of s = " + str(s.getID()))
s.incrementID()
print("ID of S incremented")
print("ID of s = " + str(s.getID()))

k = Singleton.getInstance()

print("ID of k = " + str(s.getID()))


