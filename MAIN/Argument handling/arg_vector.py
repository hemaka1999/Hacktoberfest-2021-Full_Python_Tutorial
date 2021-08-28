import sys
import getopt
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

file_name=sys.argv[1]
message=sys.argv[2]

with open(file_name,'w+') as f:
    f.write(message)

opts,args=getopt.getopt(sys.argv[1:],"f:m:",["filename",'message'])
print(opts)
print(args)
filename="test1"
mes="Default"
for opt,arg in opts:
    if opt=="-f":
        filename=arg
    if opt=="-m":
        mes=arg

with open(filename,"w+") as f:
    f.write(mes)

