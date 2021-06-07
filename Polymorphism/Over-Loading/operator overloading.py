class ComplexNumber():
    def __init__(self,real,imaginary):
        self.real=real
        self.ima=imaginary

    def __add__(self, other):
        if self.ima+other.ima>=0:
            s='{}+{}i'.format(self.real+other.real,self.ima+other.ima)
        else:
            s='{}{}i'.format(self.real+other.real,self.ima+other.ima)
        return s
    def __sub__(self, other):
        if self.ima-other.ima>=0:
            s='{}+{}i'.format(self.real-other.real,self.ima-other.ima)
        else:
            s='{}{}i'.format(self.real-other.real,self.ima-other.ima)
        return s
    def __str__(self):
        if self.ima >=0:
            s='{}+{}i'.format(self.real,self.ima)
        else:
            s='{}+{}i'.format(self.real,self.ima)
        return s
    def __mul__(self, other):
        if self.ima*other.ima>=0:
            s='{}+{}i'.format(self.real*other.real,self.ima*other.ima)
        else:
            s='{}{}i'.format(self.real*other.real,self.ima*other.ima)
        return s
    def __truediv__(self, other):
        if self.ima/other.ima>=0:
            s='{}+{}i'.format(self.real/other.real,self.ima/other.ima)
        else:
            s='{}{}i'.format(self.real/other.real,self.ima/other.ima)
        return s
    def __floordiv__(self, other):
        if self.ima//other.ima>=0:
            s='{}+{}i'.format(self.real//other.real,self.ima//other.ima)
        else:
            s='{}{}i'.format(self.real//other.real,self.ima//other.ima)
        return s

if __name__=='__main__':
    a=ComplexNumber(11,12)
    b=ComplexNumber(1,2)
    print("a:",a)
    print('b:',b)
    print("a+b",a+b)
    print('a-b',a-b)
    print('a*b:',a*b)
    print('a/b:',a/b)
    print('a//b:',a//b)
