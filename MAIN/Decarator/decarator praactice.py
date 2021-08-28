def decarator(function):
    def wrapper(*args,**kwargs):
        return_value=function(*args,*kwargs)
        with open("logfile.txt",'a+') as f:
            print(return_value)
            f.write(str(return_value))
        return return_value
    return wrapper

@decarator
def add(x,y):
    return x+y

add(90,20)
