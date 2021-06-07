#there are differnt ways to create a thread in python
#1. creating a thread without using any class
#2. creating a thread by extending thread class
#3. creating a thread without extending any class



#1. Creating a thread without using any class
from threading import *
def display():
    for i in range(-10,1):
        print("Child Thread:",i)



#creating a thread using display() method
objT = Thread(target = display)
objT.start() #it executes run(), sends thread object in Running status
#display()
for i in range(1, 11):
    print("Main Thread: ", i)

#Note: in case of multiple threads, the excecution order of
    #those threads can not be predicted
#This order of execution differe from Computer-to-Computer and Run-to-Run.
