from collections import defaultdict
x=dict()
x={
    4:'dla',
   2:'madhu',
    5:'kl'
   }
x[4]="fff"
print(x)
print(type(x))
x.pop(4)
print(x)
y=x.copy()
print(y)
x.update({77:"lal"})#update
y=x.items()
print(y)
print(type(y)) #convert into dictionary
x=defaultdict(lambda :'lal')
print(x[6])
for x,y in x.items():
    print(f"{x}:{y}")


