#method overloading using default parameter
def calc(a=None, b=None, c=None, d=None):
    if a==None and b==None and c==None:
        return None
    elif a!=None and b!=None and c!=None and d!=None:
        return a + b + c + d
    elif a!=None and b!=None and c!=None:
        return a + b + c
    elif a!=None and b!=None:
        return a + b
    elif a!=None:
        return a



if __name__=="__main__":
    #calling with no parameters
    result = calc()
    print("Result: ", result)

    #calling with one parameter
    result = calc(10)
    print("Result: ", result)



    #calling with two parameters
    result = calc(10, 20)
    print("Result: ", result)



    #calling with three paramenters
    result = calc(10, 20, 30)
    print("Result: ", result)
    #TypeError: calc() takes 2 positional arguments but 3 were given



    #calling with four parameters
    result = calc(10, 20, 30, 40)
    print("Result: ", result)
