from train import Train
from trainmgmt import Trainmgmt
from user import User
import random
import time

if(__name__ == "__main__"):
    username = "Admin"
    password = "Admin@123"
    choice = 0
    while(choice!=3):
        print("\n\t1.Admin")
        print("\n\t2.User")
        print("\n\t3.Exit")
        choice = int(input("Enter a your choice: "))

        if(choice == 1):
            username1 = input("Enter a username1: ")
            password1 = input("Enter a password1: ")
            if(username == username1 and password==password1):
                print("credential match ")
                print("login successful")    
             
            else:
                print("access denied ")
                break
            print("Most Welcome to IRCTC")    
            choice = 0
            while(choice != 5):
                    print("\t\t1.add new train")
                    print("\t\t2.view all trains")
                    print("\t\t3.search a train")
                    print("\t\t4.delete a train")
                    print("\t\t5.edit a train")

                    choice = int(input("Enter a choice: "))
                    if(choice == 1 ):
                        tid = int(input("Enter a id: "))
                        tname = input("Enter a tname: ")
                        fromstation_tostation = input("Enter a fromstation_tostation: ")
                        seats = int(input("Enter a seats: "))
                        fare = int(input("Enter a fare: "))
                        arrival_time = input("Enter a arrival time h:m:s: ")
                        departure_time = input("Enter a departure time h:m:s: ")
                        t1  = Train(tid,tname,fromstation_tostation,seats,fare,arrival_time,departure_time)
                        Trainmgmt.addRecord(t1)

                    elif(choice == 2):
                        Trainmgmt.readRecord()
                    
                    elif(choice == 3):
                        tid = int(input("Enter the tid to be search: "))
                        Trainmgmt.searchRecord(tid)
                    
                    
                    elif(choice == 4):
                        tid = int(input("Enter the tid to be delete: "))
                        Trainmgmt.deleteRecord(tid)
                    
                    elif(choice == 5):
                        tid = int(input("Enter the tid to be modify: "))
                        Trainmgmt.modifyRecord(tid)

                    else:
                        print("invalid")   
            
        elif(choice == 2):
            choice = 0
            while(choice != 6):
                print("\t\t1.show all trains")
                print("\t\t2.search a train")
                print("\t\t3.Book a ticket")
                print("\t\t4.ticket history")
                print("\t\t5.cancel a ticket")
                choice = int(input("Enter a choice: "))
                if(choice == 1):
                   Trainmgmt.readRecord()
                   
                
                elif(choice == 2):
                    tid = int(input("Enter the tid to be search: "))
                    Trainmgmt.searchRecord(tid)
                
                elif(choice == 3):
                    tid = int(input("Enter a tid for booking ticket: "))
                    n = int(input("How many tickets you want?: "))
                    for i in range(n):
                        Pnr = random.randint(111111,999999)
                        name = input("Enter a name: ")
                        age = int(input("Enter a age: "))
                        mob_no = int(input("Enter a mob_no: "))
                        gender = input("Enter a gender m/f?: ")
                        t1 = User(Pnr,name,age,mob_no,gender)
                        Trainmgmt.book_Ticket(tid,t1)  

                elif(choice==4):
                    Trainmgmt.ticket_history()         

                elif(choice==5):
                    Pnr = int(input("Enter a pnr to be cancelled: "))
                    Trainmgmt.cancel_Ticket(Pnr)

                else:
                    print("invalid operation")
                

        else:
            print("Thank You")     


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
                            break


                def cancel_Ticket(Pnr):
        try:
            fp = open("ticket_history.txt","r")            
        except FileNotFoundError:
            print("File does not exist")
        else:            
            found = False
            allTrain = []
            for line in fp: 
                line = line.strip()
                line = line.split(",")
                if(Pnr == int(line[0])):
                    found = True
                else:
                    allTrain.append(line)
            
            fp.close()
            if(found):
                fp = open("ticket_history.txt","w")
                for train in allTrain:
                    train = ",".join(train)
                    train +="\n"
                    fp.write(train)
                fp.close()
                print("ticket cancelled successfully..")
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
                        print("ticket booked successfully..")
                                
                    fp.close()            
                    fp = open("train.txt","a")
                    for train in alltrain:
                        train = ",".join(train)
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
