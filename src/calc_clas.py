#from src.calculator import mysum,divide
#import src.calculator as clc
from src.calculator import mysum,divide
class FooCalculator:
    def __init__(self):
        pass

    def somma(self,m,n):
        return mysum(m,n)

    def divisione(self,m,n):
        return divide(m,n)

test=FooCalculator
a=-9
b=-2
print("test.sum->",a,"+",b,"=",test.somma(test,a,b))
a=-21
b=3
print("test.divide->",a,":",b,"=",test.divisione(test,a,b))
