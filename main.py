from simple_term_menu import TerminalMenu
import matplotlib.pyplot as plt
from sympy import *
from math import *
import pickle
import os

#Menu's
Main_menu = ["Insert data","Least squares Method","Least rectangles Method",'Exit']
Squ_Menu  = ["Calculate the regression line Dy/x","Calculate the regression line Dx/y","Interpret the results","Draw the regression lines","Main menu"]
Rec_Menu  = ["Calculate U1 / U2","Interpret the results","Draw the regression lines","Main menu"]
Sub_menu1 = ["Enter data","Restore data","Back up data"]
Sub_menu2 = ["Draw the line Dy/x","Draw the line Dx/y","Both"]
Sub_menu3 = ["D:u1","D:u2","Both"]

#Declaration
table_x,table_y=([] for i in range(0,2))
Lambda=[]
Previous_Menu=Main_menu

##Calculation
def FillTable():
    for i in range (0,int(input("How many value would you like to enter? "))):
        table_x.append(float(input(f"Type value number X{i+1} ")))
        table_y.append(float(input(f"Type value number Y{i+1} ")))

def Average (T): return sum(T)/len(T)

def Cov(X,Y): return (sum(x*y for x,y in zip(X,Y) ))/len(X) - Average(X)* Average(Y)

def Var(V): return (sum(pow(v,2) for v in V))/len(V) - pow(Average(V),2)

##File actions
def Savedata():
    if len(table_x)==0 or len(table_y)==0: print("No data to save!")
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
        ShowTables()
    else: print("No data to load!")

##Tables actions
def ShowTables():
    print("The tables are:")
    print("Table x: ",table_x)
    print("Table y: ",table_y)

def Cleartables():
    table_x.clear()
    table_y.clear()

#Graph
def Draw():
    plt.plot(table_x,table_y,'.')
    if   Sol_Choice=="LS":
        if Choice in ['Draw the line Dy/x','Both']:
            plt.plot(table_x,[a*x+b for x in table_x],label=f"{round(a,2)}X+{round(b,2)}")
        if Choice in ['Draw the line Dx/y','Both']:
            plt.plot(table_x,[a_*x+b_ for x in table_x],label=f"{round(a_,2)}X+{round(b_,2)}")
    elif Sol_Choice=="LR":
        if Choice in ['D:u1','Both']:
            plt.plot(table_x,[D_u1.subs(x,X) for X in table_x],label=f"{D_u1}")
        if Choice in ['D:u2','Both']:
            plt.plot(table_x,[D_u2.subs(x,X) for X in table_x],label=f"{D_u2}")
    plt.legend()
    plt.show()

def Interpret():
    r = Cov(table_x,table_y) / (sqrt(Var(table_x))*(sqrt(Var(table_y))))
    print(f"r={r}")
    if   round(r) ==  1: print("Perfect positive correlation!\n")
    elif round(r) ==  0: print("No correlation!\n")
    elif round(r) == -1: print("Perfect negative correlation!\n")

def CheckEmpty():
    if len(table_x)==0 or len(table_y)==0:
        print("The tables are empty!")
        ShowMenu(Previous_Menu)
##Calculate
def ShowResults():
    print(f"x̄={round(Average(table_x),2)}")
    print(f"ȳ={round(Average(table_y),2)}")
    print(f"Var(x)={round(Var(table_x),2)}")
    print(f"Var(y)={round(Var(table_y),2)}")
    print(f"Cov(x,y)={round(Cov(table_x,table_y),2)}")


def Lr_Calculate():
    CheckEmpty()
    V=[[Var(table_x),Cov(table_x,table_y)],[Cov(table_x,table_y),Var(table_y)]]
    A=1
    B=-V[0][0]-V[1][1]
    C=round(V[0][0]*V[1][1] - pow(Cov(table_x,table_y),2),2)
    Delta(A,B,C)
    Solve_eq()

def Ls_Calculate():
    CheckEmpty()
    global a,b,a_,b_
    a = Cov(table_x,table_y) / Var(table_x)
    b = Average(table_y) - a * Average(table_x)
    alpha=Cov(table_x,table_y) / Var(table_x)
    beta=Average(table_x) - alpha * Average(table_y)
    a_= 1/alpha
    b_= -beta/alpha

def Lr_Results():
    print(f"lambda1= {Lambda[0]}")
    print(f"lambda2= {Lambda[1]}")
    print(f"Du1:x2 = {D_u1}")
    print(f"Du2:x2 = {D_u2}")

def Ls_Results():
    if Choice == 'Calculate the regression line Dy/x':
        print(f"Dy/x:y = {round(a,2) }X+ {round(b,2)}")
    else:
        print(f"Dx/y:y = {round(a_,2)}X+ {round(b_,2)}")

def Solve_eq():
    global D_u1,D_u2,x

    x = symbols('x')
    y = symbols('y')

    varx_l  = round(Var(table_x)-Lambda[0],2)
    vary_l  = round(Var(table_y)-Lambda[1],2)
    covar_l = round(Cov(table_x,table_y),2)
    
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

    D_u1= (U1[1] / U1[0])* x + Average(table_x) - (U1[1] / U1[0])* Average(table_y)
    D_u2= (U2[1] / U2[0])* x + Average(table_x) - (U2[1] / U2[0])* Average(table_y)

def Delta(A,B,C):
    global Lambda
    D= pow(B,2) - 4* A * C
    Lambda.clear()
    if D>0:
        Lambda.append(round((-B-sqrt(D)) / (2*A),2))
        Lambda.append(round((-B+sqrt(D)) / (2*A),2))
        Lambda.sort(reverse = True)
    elif D==0:
        Lambda.append((-B) / (2*A))
        print(f"lambda= {Lambda[0]}")
    else:
        print("There is no solution! you may have to check the inputs")

##Menu
def ShowMenu(Menu):
    global Choice
    terminal_menu = TerminalMenu(Menu)
    Choice_index = terminal_menu.show()
    Choice=Menu[Choice_index]
    Redirect(Choice)

##Redirect
def Redirect(Choice):
    global Sol_Choice,Previous_Menu
    while True:
        os.system('clear')
        ##Main Menu
        if   Choice == "Insert data": ShowMenu(Sub_menu1)
        elif Choice == 'Enter data': FillTable()
        elif Choice == 'Restore data': Loaddata()
        elif Choice == 'Back up data': Savedata()

        elif Choice == "Least squares Method": 
            Ls_Calculate()
            Sol_Choice="LS"
            Previous_Menu=Squ_Menu
            ShowMenu(Squ_Menu)
        elif Choice == "Least rectangles Method": 
            Lr_Calculate()
            Sol_Choice="LR"
            Previous_Menu=Rec_Menu
            ShowMenu(Rec_Menu)
        elif Choice == "Exit": exit()
    
        #Squ_Menu
        elif Choice in ["Calculate the regression line Dy/x","Calculate the regression line Dx/y"]: 
            ShowResults()
            Ls_Results()
        elif Choice == "Calculate U1 / U2":
            ShowResults()
            Lr_Results()
        
        #Square Menu + Rectangle Menu
        elif Choice == "Interpret the results": Interpret()
        elif Choice == "Draw the regression lines":
            if Sol_Choice=="LS":
                ShowMenu(Sub_menu2)
            elif Sol_Choice=="LR":
                ShowMenu(Sub_menu3)
        elif Choice == "Main menu": ShowMenu(Main_menu)

        #Draw Menu
        elif Choice in Sub_menu2 or Choice in Sub_menu3:
                Draw()

        ShowMenu(Previous_Menu)

ShowMenu(Main_menu)

