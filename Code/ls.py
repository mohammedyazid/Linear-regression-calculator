##Packages
from Code.general_calcul import calcul
import matplotlib.pyplot as plt
from sympy import *
from math import *

class less_squares():
    # ab=[a,b,a_,b_]
    ab=[]

    def Ls_Calculate(self,X,Y):
        clc = calcul()
        self.ab.append(clc.Cov(X,Y) / clc.Var(X))
        self.ab.append(clc.Average(Y) - self.ab[0] * clc.Average(X))
        alpha=clc.Cov(X,Y) / clc.Var(X)
        beta=clc.Average(X) - alpha * clc.Average(Y)
        self.ab.append(1/alpha)
        self.ab.append(-beta/alpha)

    def Ls_Results(self,Choice):
        if Choice == 'Calculate the regression line Dy/x':
            print(f"Dy/x:y = {round(self.ab[0],2) }X+ {round(self.ab[1],2)}")
        else:
            print(f"Dx/y:y = {round(self.ab[2],2)}X+ {round(self.ab[3],2)}")
    
    def Draw(self,X,Y,Choice):
        plt.plot(X,Y,'.')
        if Choice in ['Draw the line Dy/x','Both']:
            plt.plot(X,[self.ab[0]*x+self.ab[1] for x in X],label=f"{round(self.ab[0],2)}X+{round(self.ab[1],2)}")
        if Choice in ['Draw the line Dx/y','Both']:
            plt.plot(X,[self.ab[2]*x+self.ab[3] for x in X],label=f"{round(self.ab[2],2)}X+{round(self.ab[3],2)}")
 
        plt.legend()
        plt.show()