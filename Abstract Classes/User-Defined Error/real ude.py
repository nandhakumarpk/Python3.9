#How to create user define Exception



#syntax
'''
class ExceptionClassName(PredefinedExceptionName):
def __init__(self, arg):
self.msg = arg



'''
#every Exception class in python is defined from upper level class Exception
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg
'''
#How to raise user defined Exception explicitly, using keyword 'raise'
raise TooYoungException("Too Young to get marry")
'''



class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg



#main module
if __name__ == "__main__":
    age = int(input("Enter your age: "))
    if age < 18:
        raise TooYoungException("You are too young to get marry, wait some time to get best match")
    elif age > 60:
        raise TooOldException("You already crossed marriage age")
    else:
        print("Best match is being searched, you will get notified through email")

