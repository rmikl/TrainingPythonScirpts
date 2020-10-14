from datetime import datetime
from time import time 

def sampleMethod():
    print("method execution")

def check_exec_time():
    start_time = time()
    sampleMethod()
    end_time = time()
    result = end_time - start_time
    return result

print(check_exec_time())