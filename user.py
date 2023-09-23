class User:
    def __init__(self,pnr,name,age,gender,mob):
        self.pnr = pnr
        self.name = name
        self.age = age
        self.gender = gender 
        self.mob = mob
        


    def __str__(self):
        data = str(self.pnr)+","+ str(self.name)+","+str(self.age) +","+str(self.gender) +","+str(self.mob)
        return data 

    

                       
     

