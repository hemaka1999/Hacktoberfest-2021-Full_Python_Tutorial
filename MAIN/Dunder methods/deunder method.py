nums=[1,2,3,4,5,6]
print(len(nums))
print(nums.__len__())


class Account:

   def __init__(self, account_name, balance=0):

       self.account_name = account_name

       self.balance = balance

   def __add__(self,acc):

       if isinstance(acc,Account):

           return self.balance  + acc.balance

       raise Exception(f"{acc} is not of class Account")


a1=Account("lal",4444)
a2=Account("kal",55555)
a3=Account("jeel",34343)
print(a1+a2)

