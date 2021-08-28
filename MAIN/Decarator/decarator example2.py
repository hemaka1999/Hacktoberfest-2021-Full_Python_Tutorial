import time
def timed(function):
    def wrapper(*args,**kwargs):
        before=time.time()

        return_value=function(*args,**kwargs)
        after=time.time()

        duration=after-before
        fname=function.__name__
        print(f"{fname} duration is {duration}")
        return return_value
    return wrapper

@timed
def void_function(x,y):
    return x+y

@timed
def for_function(j):
    result = 1
    for i in range(1,j):
        result=result+i
    return result

@timed
def dual_for_function():
    for i in range(1,100):
        for j in range(1,1000):
            i*j



void_function(10000000,643487394739479724972394)
for_function(10000000)
dual_for_function()