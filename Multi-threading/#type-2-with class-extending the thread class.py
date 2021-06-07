#there are differnt ways to create a thread in python
#1. creating a thread without using any class
#2. creating a thread by extending thread class
#3. creating a thread without extending any class



#2. Creating a Thread by extending Thread Class
#Thread is the base class for any thread, we can user this class to derive user-defined Thread class
#Thread class has start() which enforce to execute run() method
from threading import *
class MyThread(Thread):
#overridding run() method
    def run(self):
        for i in range(1, 11):
            print("Child Thread: ", i)



#create MyThread object
obj = MyThread()
obj.start() #this will enforce to execute run() method
#statement from main thread
for i in range(1, 11):
    print("Main Thread: ", i)
