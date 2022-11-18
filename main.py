from math import *
import pickle
from simple_term_menu import TerminalMenu
import os
import matplotlib.pyplot as plt

Main_menu=["Insert data","Calculate the regression line Dy/x","Calculate the regression line Dx/y","Interpret the results","Draw the regression line",'Exit']
Sub_menu1=["Enter data","Restore data","Back up data"]
Sub_menu2=["Draw the line Dy/x","Draw the line Dx/y","Both"]
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
    if Choice == 'Calculate the regression line Dy/x':
        print(f"a={round(a,2)}\nb={round(b,2)}")
        print(f"S_ex={round(S_ex,2)}\nS_ey={round(S_ey,2)}")
    elif Choice == 'Calculate the regression line Dx/y':
        print(f"a={round(a_,2)}\nb={round(b_,2)}")
        print(f"S_ex={round(S_ex,2)}\nS_ey={round(S_ey,2)}")

def Interpret():
    print(f"r={r}")
    if round(r)==1: print("Perfect positive correlation!\n")
    elif round(r)==0: print("No correlation!\n")
    elif round(r)==-1: print("Perfect negative correlation!\n")

def Draw():
    plt.plot(table_x,table_y,'.')
    if Choice == 'Draw the line Dy/x' or Choice == 'Both':
        plt.plot(table_x,[a*x+b for x in table_x],label=f"{round(a,2)}X+{round(b,2)}")
    if Choice == 'Draw the line Dx/y' or Choice == 'Both':
        plt.plot(table_x,[a_*x+b_ for x in table_x],label=f"{round(a_,2)}X+{round(b_,2)}")
    plt.legend()
    plt.show()

def Calculate():
    global X_Bar,Y_Bar,Var_X,Var_Y,Covar,a,b,S_ex,S_ey,r,alpha,beta,a_,b_
    if len(table_x)==0 or len(table_y)==0:
        print("The tables are empty!")
        Menu(Main_menu)
    else:
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

def Savedata():
    if len(table_x)==0 or len(table_y)==0:
        print("No data to save!")
    else:
        with open("data",'wb') as file:
            pickle.dump(table_x, file)
            pickle.dump(table_y, file)
        print("Data saved successfully!")

def Loaddata():
    global table_x,table_y
    if os.path.isfile('data'):
        with open("data", 'rb') as file:
            table_x=pickle.load(file)
            table_y=pickle.load(file)
        print("Data loaded successfully!")
        print("The tables are:")
        print("Table x: ",table_x)
        print("Table y: ",table_y)
    else:
        print("No data to load!")
    
def Cleartables():
    table_x.clear()
    table_y.clear()

def Menu(MenuName):
    global Choice
    while True:
        terminal_menu = TerminalMenu(MenuName)
        choice_index = terminal_menu.show()
        Choice=MenuName[choice_index]
        os.system('clear')
        if Choice == 'Insert data':
            Menu(Sub_menu1)
        elif Choice == 'Calculate the regression line Dy/x': 
            Calculate()
            Regression()
        elif Choice == 'Calculate the regression line Dx/y': 
            Calculate()
            Regression()
        elif Choice == 'Interpret the results': 
            Calculate()
            Interpret()
        elif Choice == 'Draw the regression line':
            Menu(Sub_menu2)
        elif Choice == 'Enter data': FillTable()
        elif Choice == 'Restore data': Loaddata()
        elif Choice == 'Back up data': Savedata()
        elif Choice in ["Draw the line Dy/x","Draw the line Dx/y","Both"]: Calculate();Draw()
        else : exit()
        MenuName=Main_menu

#   Main Program
Menu(Main_menu)

