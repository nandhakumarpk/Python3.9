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



#How to raise user defined Exception explicitly, using keyword 'raise'
raise TooYoungException("Too Young to get marry")
