import threading
import time

def print_name(name,*args):
    print(name,*args)


name = "Tutorialspoint..."

thread1 = threading.Thread(target=print_name,args=(name,1))
thread2 = threading.Thread(target=print_name,args=(name,1,2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Threads are finished...exiting")\

    
