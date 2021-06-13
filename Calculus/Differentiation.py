'''Requirement 'sympy'
If you haven't installed it install it by opening your terminator or command prompt then type the following command
pip install sympy
then wait for it to install
if you check if you have installed it or not you can check it by typing pip list after that and check if it is preinstalled it there or not'''


import sympy as sym
def differentiate(exp,var,times=1):
    return sym.diff(exp,var,times)

def main():
    exp=input("Enter the expression: ")
    var=input("Enter variable with respect to you want to differntiate: ")
    var=sym.Symbol(var)
    times=int(input("Enter the nth derverivative you want: "))
    for i in range(1,times+1):
        print("Differentiation after {}th time is {}".format(i,differentiate(exp,var,i)))
    
if __name__=='__main__':
    main()
