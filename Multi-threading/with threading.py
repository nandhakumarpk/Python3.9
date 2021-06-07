from threading import *
import time
def doublesN(numList):
    for n in numList:
        print("Doubles: ", 2*n)



def squaresN(numList):
    for n in numList:
        print("Squares: ", n*n)

if __name__=="__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #create a thread with doublesN() method
    thread1 = Thread(target = doublesN, args=(numbers,))
    thread2 = Thread(target = squaresN, args=(numbers,))
    beginTime = time.time() #this stores current time of system
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Time Taken: ", time.time()-beginTime)
