def calc(*var):
    s = 0
    for i in var:
        s = s + i
    return s



if __name__=="__main__":
    result = calc()
    print("Result: ", result)



    result = calc(10)
    print("Result: ", result)



    result = calc(10, 20)
    print("Result: ", result)



    result = calc(10, 20, 30)
    print("Result: ", result)



    result = calc(10, 20, 30, 40)
    print("Result: ", result)



    result = calc(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print("Result: ", result)
