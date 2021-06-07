def method(a=None, b=None, c=None):
    if a!=None and b!=None and c!=None:
        return a + b + c
    elif a!=None and b!=None:
        return a * b
    else:
        return "Parameter Missing"



if __name__=="__main__":
    result = method()
    print("Result: ", result)



    result = method(10, 20)
    print("Result: ", result)



    result = method(10, 20, 30)
    print("Result: ", result)
