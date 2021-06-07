class Object:
    pass

class D(Object):
    pass

class E(Object):
    pass

class F(Object):
    pass

class B(E,D):
    pass

class C(F,D):
    pass

class A(B,C):
    pass

if __name__=='__main__':
    print(Object.mro(),'\n\n')
    print(D.mro(),'\n\n')
    print(E.mro(),'\n\n')
    print(F.mro(),'\n\n')
    print(B.mro(),'\n\n')
    print(C.mro(),'\n\n')
    print(A.mro(),'\n\n')
    
