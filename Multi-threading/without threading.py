#without Multi Threading
from threading import *
import time
def doublesN(numList):
    for n in numList:
        print("Doubles: ", 2*n)



def squaresN(numList):
    for n in numList:
        print("Squares: ", n*n)



#main module
if __name__=="__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    beginTime = time.time() #this stores current time of system
    doublesN(numbers)
    squaresN(numbers)
    endTime = time.time()
    ellapsed = endTime-beginTime
    print("Time Taken: ", ellapsed)
