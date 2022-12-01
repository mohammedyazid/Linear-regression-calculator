from Code import *
from simple_term_menu import TerminalMenu

#Menu's
Main_menu = ["Insert data","Least squares Method","Least rectangles Method",'Exit']
Squ_Menu  = ["Calculate the regression line Dy/x","Calculate the regression line Dx/y","Interpret the results","Draw the regression lines","Main menu"]
Rec_Menu  = ["Calculate U1 / U2","Interpret the results","Draw the regression lines","Main menu"]
Sub_menu1 = ["Enter data","Restore data","Back up data"]
Sub_menu2 = ["Draw the line Dy/x","Draw the line Dx/y","Both"]
Sub_menu3 = ["D:u1","D:u2","Both"]

class main():
    #Declaration
    table_x,table_y=([] for i in range(0,2))
    Lambda=[]
    Previous_Menu=Main_menu

    def ShowMenu(self,Menu):
        terminal_menu = TerminalMenu(Menu)
        Choice_index = terminal_menu.show()
        Choice=Menu[Choice_index]
        self.Redirect(Choice)

    ##Redirect
    def Redirect(self,Choice):
        act = actions()
        ls = less_squares()
        lr = less_rectangles()
        clc= calcul()
        while True:
            os.system('clear')
            ##Main Menu
            if   Choice == "Insert data":  self.ShowMenu(Sub_menu1)
            elif Choice == 'Enter data':   actions.FillTable(self.table_x,self.table_y)
            elif Choice == 'Restore data': 
                                           self.table_x,self.table_y =act.Loaddata()
                                           act.ShowTables(self.table_x,self.table_y)
            elif Choice == 'Back up data': act.Savedata(self.table_x,self.table_y)

            elif Choice == "Least squares Method":
                                           if act.CheckEmpty(self.table_x,self.table_y):pass
                                           else:
                                                ls.Ls_Calculate(self.table_x,self.table_y)
                                                self.Sol_Choice="LS"
                                                self.Previous_Menu=Squ_Menu
                                                self.ShowMenu(Squ_Menu)

            elif Choice == "Least rectangles Method":
                                           if act.CheckEmpty(self.table_x,self.table_y):pass
                                           else:
                                                act.CheckEmpty(self.table_x,self.table_y) 
                                                lr.Lr_Calculate(self.table_x,self.table_y)
                                                self.Sol_Choice="LR"
                                                self.Previous_Menu=Rec_Menu
                                                self.ShowMenu(Rec_Menu)
            elif Choice == "Exit":        exit()
        
            elif Choice in ["Calculate the regression line Dy/x","Calculate the regression line Dx/y"]: 
                                           clc.ShowResults(self.table_x,self.table_y)
                                           ls.Ls_Results(Choice)

            elif Choice == "Calculate U1 / U2":
                                           clc.ShowResults(self.table_x,self.table_y)
                                           lr.Lr_Results()

            elif Choice == "Interpret the results": clc.Interpret(self.table_x,self.table_y)
            elif Choice == "Draw the regression lines":
                if self.Sol_Choice=="LS":  self.ShowMenu(Sub_menu2)
                elif self.Sol_Choice=="LR":self.ShowMenu(Sub_menu3)
            elif Choice == "Main menu":    self.ShowMenu(Main_menu)

            #Draw Menu
            elif Choice in Sub_menu2 and self.Sol_Choice=="LS":      
                                           ls.Draw(self.table_x,self.table_y,Choice)
            elif Choice in Sub_menu3 and self.Sol_Choice=="LR":      
                                           lr.Draw(self.table_x,self.table_y,Choice)
            
            self.ShowMenu(self.Previous_Menu)

main = main()
main.ShowMenu(Main_menu)

