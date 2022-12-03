import pickle
import os
class actions():
    ##Tables actions
    def FillTable(X,Y):
        for i in range (0,int(input("How many value would you like to enter? "))):
            X.append(float(input(f"Type value number X{i+1} ")))
            Y.append(float(input(f"Type value number Y{i+1} ")))

    def ShowTables(self,X,Y):
        print("The tables are:")
        print("Table x: ",X)
        print("Table y: ",Y)

    def Cleartables(X,Y):
        return X.clear(),Y.clear()    

    def CheckEmpty(self,X,Y):
        if len(X)==0 or len(Y)==0:
            print("The tables are empty!")
            return True
        else:
            return False

    ##File actions
    def Savedata(self,X,Y):
        if len(X)==0 or len(Y)==0: print("No data to save!")
        else:
            with open("Code/data",'wb') as file:
                pickle.dump(X, file)
                pickle.dump(Y, file)
            print("Data saved successfully!")

    def Loaddata(self):
        if os.path.isfile('Code/data'):
            with open("Code/data", 'rb') as file:
                X=pickle.load(file)
                Y=pickle.load(file)
            print("Data loaded successfully!")
            return X,Y
        else: print("No data to load!")