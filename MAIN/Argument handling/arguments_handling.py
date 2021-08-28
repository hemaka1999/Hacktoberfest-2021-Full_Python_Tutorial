def arguments(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['key1'])
    print(kwargs['key2'])

arguments("hi","bro",True,567,key1="lal",key2=45)

    