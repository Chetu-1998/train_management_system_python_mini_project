from datetime import timedelta
class Train:
    def __init__(self,tid,tname,fromstation_tostation,seats,fare,arrival_time,departure_time):
        self.tid = tid
        self.tname = tname
        self.fromstation_tostation = fromstation_tostation 
        self.seats = seats
        self.fare = fare
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        

    def __str__(self):
        data = str(self.tid)+","+str(self.tname) +","+str(self.fromstation_tostation)+","+str(self.seats)+","+str(self.fare)+","+str(self.arrival_time)+","+str(self.departure_time)
        return data 
