while 1:
    a=10
    try:
        a=20    
        i=int(input("Enter a number: "))
        a=30
        print('a',a)
    except ValueError:
        print('a',a)
        print("Please type a number")
    except ZeroDivisionError:
            print("0 division error")
            

