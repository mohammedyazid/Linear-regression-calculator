import matplotlib.pyplot as plt
from sympy import *
from math import *

class calcul():
    def Average (self,T): return sum(T)/len(T)

    def Cov(self,X,Y): return (sum(x*y for x,y in zip(X,Y) ))/len(X) - self.Average(X)* self.Average(Y)

    def Var(self,V): return (sum(pow(v,2) for v in V))/len(V) - pow(self.Average(V),2)

    def Interpret(self,X,Y):
        r = self.Cov(X,Y) / (sqrt(self.Var(X))*(sqrt(self.Var(Y))))
        print(f"r={r}")
        if   round(r) ==  1: print("Perfect positive correlation!\n")
        elif round(r) ==  0: print("No correlation!\n")
        elif round(r) == -1: print("Perfect negative correlation!\n")

    ##Calculate
    def ShowResults(self,X,Y):
        print(f"x̄={round(self.Average(X),2)}")
        print(f"ȳ={round(self.Average(Y),2)}")
        print(f"Var(x)={round(self.Var(X),2)}")
        print(f"Var(y)={round(self.Var(Y),2)}")
        print(f"Cov(x,y)={round(self.Cov(X,Y),2)}")