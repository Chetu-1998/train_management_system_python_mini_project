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
                print("login successful")    
             
            else:
                print("access denied ")
                break   
            choice = 0
            while(choice != 5):
                    print("\t\t1.add new train")
                    print("\t\t2.view all trains")
                    print("\t\t3.search a train")
                    print("\t\t4.edit a train")
                    print("\t\t5.delete a train")

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
                        tid = int(input("Enter the tid to be modify: "))
                        Trainmgmt.modifyRecord(tid)

                    elif(choice == 5):
                        tid = int(input("Enter the tid to be delete: "))
                        Trainmgmt.deleteRecord(tid)
                    
                    
                    else:
                        print("invalid")   
            
        elif(choice == 2):
            choice = 0
            print("Most welcome to IRCTC")
            while(choice != 6):
                print("\t\t1.show all trains")
                print("\t\t2.search a train")
                print("\t\t3.Book a ticket")
                print("\t\t4.ticket history")

                choice = int(input("Enter a choice: "))
                if(choice == 1):
                   Trainmgmt.readRecord()
                   
                
                elif(choice == 2):
                    tid = int(input("Enter the tid to be search: "))
                    Trainmgmt.searchRecord(tid)
                
                elif(choice == 3):
                    tid = int(input("Enter a tid for booking ticket: "))
                    Trainmgmt.book_Ticket(tid)  
                
                elif(choice==4):
                    Trainmgmt.ticket_history()         

                else:
                    print("invalid operation")
                

        else:
            print("Thank You")           
