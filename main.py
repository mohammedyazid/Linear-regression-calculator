from math import *
from simple_term_menu import TerminalMenu
import os
import matplotlib.pyplot as plt

options = ['Add variables to the tables', 'Calculate the regression line.', 'interpret the results.', 'Draw the regression line', 'Exit']
table_x,table_y=([] for i in range(0,2))

def Average (T): return sum(T)/len(T)

def Cov(X,Y): return (sum(x*y for x,y in zip(X,Y) ))/len(X) - Average(X)* Average(Y)

def Var(V): return (sum(pow(v,2) for v in V))/len(V) - pow(Average(V),2)

def FillTable():
    N=int(input("How many value would you like to enter? "))
    for i in range (0,N):
        table_x.append(float(input(f"Type value number X{i+1} ")))
        table_y.append(float(input(f"Type value number Y{i+1} ")))
    print("==================================================")

def Regression():
    print(f"x̄={round(X_Bar,2)}\nȳ={round(Y_Bar,2)}")
    print(f"Var(x)={round(Var_X,2)}\nVar(y)={round(Var_Y,2)}")
    print(f"Cov(x,y)={round(Cov(table_x,table_y),2)}")
    print(f"Dy/x:y= {round(a,2)}X + {round(b,2)}")
    print(f"Dx/y:y= {round(a_,2)}X + {round(b_,2)}")

def Interpret():
    print(f"r={r}")
    if round(r)==1: print("Perfect positive correlation!\n")
    elif round(r)==0: print("No correlation!\n")
    elif round(r)==-1: print("Perfect negative correlation!\n")

def Draw():
    plt.plot(table_x,table_y,'.')
    plt.plot(table_x,[a*x+b for x in table_x],label=f"{round(a,2)}X+{round(b,2)}")
    plt.plot(table_x,[a_*x+b_ for x in table_x],label=f"{round(a_,2)}X+{round(b_,2)}")
    plt.legend()
    plt.show()

def Calculate():
    global X_Bar,Y_Bar,Var_X,Var_Y,Covar,a,b,S_ex,S_ey,r,alpha,beta,a_,b_
    X_Bar=Average(table_x)
    Y_Bar=Average(table_y)
    Var_X=Var(table_x)
    Var_Y=Var(table_y)
    Covar=Cov(table_x,table_y)
    a=Covar/Var_X
    b=Y_Bar-a*X_Bar
    alpha=Covar/Var_Y
    beta=X_Bar-alpha*Y_Bar
    a_= 1/alpha
    b_= -beta/alpha
    S_ex=sqrt(Var(table_x))
    S_ey=sqrt(Var(table_y))
    r=Cov(table_x,table_y) / (S_ex*S_ey)

def Menu():
    while True:
        Calculate()
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        Choice=options[menu_entry_index]
        os.system('clear')
        if Choice == 'Add variables to the tables': FillTable()
        elif Choice == 'Calculate the regression line.': Regression()
        elif Choice == 'interpret the results.': Interpret()
        elif Choice == 'Draw the regression line': Draw()
        else: break
#   Main Program
FillTable()
Menu()