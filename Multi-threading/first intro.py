#threading module is used to create Thread
#or to create our derive our Thread class
import threading
print("hello world")



print("Currently Running Thread: ", threading.current_thread().getName())



#current_thread(): method returns currently running thread as object.
#getName(): is getter method of Thread object to get the
#name of currently running thread.
