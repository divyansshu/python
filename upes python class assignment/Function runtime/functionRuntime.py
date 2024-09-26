import time as t
from functionScope import add
from functionScope import sub

def  timefunction(func, *args, **kwargs):
    startTime = t.time() # record the start time
    res = func(*args, **kwargs) # call the function with the provided arguments
    endTime = t.time() # record the end time
    runTimeInSec = endTime - startTime # calculate the run time
    print(f"\n time to execute function is {runTimeInSec*1000000}  micro seconds ") # print the result in microseconds
    print(res) # print the result
    
a = 10000
b = 20000
    
timefunction(add, a ,b)
timefunction(sub, a ,b)
    


