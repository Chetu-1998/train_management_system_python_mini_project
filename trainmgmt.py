import random
from re import T
from select import select
from sys import set_asyncgen_hooks
from tkinter import E
from train import Train
class Trainmgmt:
    def addRecord(t):
        fp = open("train.txt","a")
        fp.write(str(t))
        fp.write("\n")
        fp.close()

    def readRecord():
        try:
            fp = open("train.txt","r")
        except FileNotFoundError:
            print("file does not exits")
        else:
            data = fp.read()
            print(data)
            fp.close()
    
    def searchRecord(tid):
        try:
            fp = open("train.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:             
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(tid == int(line[0])):
                    print("record found")
                    print(line)
                    break
            else:
                print("Record not found")
    
    def modifyRecord(tid):
            try:
                fp = open("train.txt","r")            
            except FileNotFoundError:
                print("File does not exist")
            else:            
                found = False
                allTrain = []
                for line in fp:
                    line = line.strip()
                    line = line.split(",")
                    if(tid == int(line[0])):
                        found = True
                        ans = input("Do you wish to change name(y/n)?")
                        if(ans.lower() == "y"):
                            line[1] = input("Enter new name: ")
                        ans = input("Do you wish to change id: (y/n)?")
                        if(ans.lower() == "y"):
                            line[0] = input("Enter new id: ")
                        
                    allTrain.append(line)
                print(allTrain)
                
                fp.close()
                if(found):
                    fp = open("train.txt","w")
                    for train in allTrain:
                        train = ",".join(train)
                        train +="\n"
                        fp.write(train)
                    fp.close()
                    print("Record edited successfully..")
                else:
                    print("Record not found")

    
    def deleteRecord(tid):
        try:
            fp = open("train.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:            
            found = False
            allTrain = []
            for line in fp:
                line = line.strip()
                line = line.split(",")
                if(tid == int(line[0])):
                    found = True
                else:
                    allTrain.append(line)
            
            fp.close()
            if(found):
                fp = open("train.txt","w")
                for train in allTrain:
                    train = ",".join(train)
                    train +="\n"
                    fp.write(train)
                fp.close()
                print("Record deleted successfully..")
            else:
                print("Record not found")
        

    def readRecord():
        try:
            fp = open("train.txt","r")
        except FileNotFoundError:
            print("file does not exits")
        else:
            data = fp.read()
            print(data)
            fp.close()


    def searchRecord(tid):
        try:
            fp = open("train.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:            
            for line in fp: 
                line = line.strip()
                line = line.split(",")
                if(tid == int(line[0])):
                    print("record found")
                    print(line)
                    break
            else:
                print("Record not found")

   
    def book_Ticket(tid):
        try:
            fp = open("train.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:
            for line in fp:         
                line = line.strip()
                line = line.split(",")
                if(tid == int(line[0])):
                    print("record found")
                    n = int(input("How many tickets you want?: "))
                    for i in range(n):
                        Pnr = random.randint(111111,999999)
                        name = input("Enter a name: ")
                        age = int(input("Enter a age: "))
                        mob_no = int(input("Enter a mob_no: "))
                        gender = input("Enter a gender m/f?: ")
                        t = [Pnr,name,age,mob_no,gender]
                        t.extend(line)
                        t.pop(8)
                        fp = open("ticket_history.txt","a")   
                        fp.write(str(t))
                        fp.write("\n")
                        fp.close()
                        fp = open("train.txt","r")
                        found = False
                        alltrain = []
                        for line in fp:
                            line = line.strip()
                            line = line.split(",")
                            seats = int(line[3])
                            if(seats == int(line[3])):
                                ans = input("book ticket: ?y/n: ")
                                if(ans.lower() == "y"):
                                    line[3] = seats - n                                                                                               
                            alltrain.append(line)
                        print(alltrain)
                        
                        
                        fp.close()            
                        fp = open("train.txt","w")
                        for train in alltrain:
                            train = ",".join(map(str,train))
                            train +="\n"
                            fp.write(train)
                        fp.close()
                        break      
                else:
                    print("record not found")  


    def ticket_history():
        try:
            fp = open("ticket_history.txt","r")
        except FileNotFoundError:
            print("file does not exits")
        else:
            data = fp.read()
            print(data)
            fp.close()










                        
                       
