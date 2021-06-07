import time
#import datetime
#from datetime import datetime
class Stopwatch:
    def __init__(self):
        self.__startTime=time.time()
        self.__endTime=0

    def start(self):
        self.__startTime=time.time()
        #print(self.__startTime)


    def stop(self):
        self.__endTime=time.time()
        #print(self.__endTime)


    def getElapsedTime(self):
        return ((self.__endTime - self.__startTime)*100)
        
if __name__=='__main__':
    s=Stopwatch()
    start=input("Enter any character to start the stop watch")
    s.start()
    end=input("Enter any character to see the elapsed time")
    s.stop()
    print(s.getElapsedTime(), 'microseconds')
    
    
