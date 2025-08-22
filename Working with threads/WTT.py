# so what is thread 
# suppose u want to download 3 files from internet , so u download them one by one , which will take lot of time 
# but if u download them in parallel then it will take less time
# so thread is like a process which can run in parallel with other process

# THIS IS THE DEMO 

import threading
import time 
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for{seconds} seconds")
    time.sleep(seconds)


time1=time.perf_counter()
#func(4)
#func(3)
#func(2)

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()
t3.start()

time2 = time.perf_counter()
print(time2-time1)




# Thread Pool Executor 


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(func, 3),
            executor.submit(func, 4),
            executor.submit(func, 1)
        ]
        for f in futures:
            print(f.result())
