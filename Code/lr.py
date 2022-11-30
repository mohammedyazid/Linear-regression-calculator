from Code.general_calcul import calcul
import matplotlib.pyplot as plt
from sympy import *
from math import *


class less_rectangles(calcul):
    Lambda,D_u=[],[]
    def Lr_Calculate(self,X,Y):
        clc = calcul()
        V=[[clc.Var(X) , clc.Cov(X,Y)],[clc.Cov(X,Y) , clc.Var(Y)]]
        A=1
        B=-V[0][0]-V[1][1]
        C=round(V[0][0]*V[1][1] - pow(clc.Cov(X,Y),2),2)
        self.Delta(A,B,C)
        self.Solve_eq(X,Y)

    def Delta(self,A,B,C):
        D= pow(B,2) - 4* A * C
        self.Lambda.clear()
        if D>0:
            self.Lambda.append(round((-B-sqrt(D)) / (2*A),2))
            self.Lambda.append(round((-B+sqrt(D)) / (2*A),2))
            self.Lambda.sort(reverse = True)
        elif D==0:
            self.Lambda.append((-B) / (2*A))
            print(f"lambda= {Lambda[0]}")
        else:
            print("There is no solution! you may have to check the inputs")

    def Solve_eq(self,X,Y):
        clc = calcul()
        x = symbols('x')
        y = symbols('y')

        varx_l  = round(clc.Var(X)-self.Lambda[0],2)
        vary_l  = round(clc.Var(Y)-self.Lambda[1],2)
        covar_l = round(clc.Cov(X,Y),2)
        
        expr1_1 = Eq((varx_l * x + covar_l * y),0)
        # expr1_2 = Eq((-0.36 * x - 0.18 * y),0)
        expr2_1 = Eq((covar_l * x + vary_l * y),0)
        # expr2_2 = Eq((-0.36 * x + 0.72 * y),0)
        sol1 = solve(expr1_1,y)
        sol2 = solve(expr2_1,y)

        u1_sqr=Eq(Pow((x),2) + Pow(sol1[0],2),1)
        u2_sqr=Eq(Pow((x),2) + Pow(sol2[0],2),1)

        final1=solve(u1_sqr)
        final2=solve(u2_sqr)

        X1=final1[1]
        X2=final2[1]

        Y1= sol1[0].subs(x,X1)
        Y2= sol2[0].subs(x,X2)

        U1=[round(X1,4),round(Y1,4)]
        U2=[round(X2,4),round(Y2,4)]

        self.D_u.append((U1[1] / U1[0])* x + clc.Average(X) - (U1[1] / U1[0])* clc.Average(Y))
        self.D_u.append((U2[1] / U2[0])* x + clc.Average(X) - (U2[1] / U2[0])* clc.Average(Y))

    def Lr_Results(self):
        print(f"lambda1= {self.Lambda[0]}")
        print(f"lambda2= {self.Lambda[1]}")
        print(f"Du1:x2 = {self.D_u[0]}")
        print(f"Du2:x2 = {self.D_u[1]}")

    def Draw(self,X,Y,Choice):
        x = symbols('x')
        plt.plot(X,Y,'.')
        if Choice in ['D:u1','Both']:
            plt.plot(X,[self.D_u[0].subs(x,X) for X in X],label=f"{self.D_u[0]}")
        if Choice in ['D:u2','Both']:
            plt.plot(X,[self.D_u[1].subs(x,X) for X in X],label=f"{self.D_u[1]}")
        plt.legend()
        plt.show()