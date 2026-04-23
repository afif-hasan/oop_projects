from ride import Ride
from pathao import Pathao
from operations import Operations
from vehicle import Vehicle

class User:
    def __init__(self,name,curr_loc,mail,password):
        self.name=name
        self.curr_loc=curr_loc
        self.mail=mail
        self.password=password
        # Pathao.list_users.append(self)

class Passenger(User):
    def __init__(self, name, curr_loc, mail, password):
        super().__init__(name, curr_loc, mail, password)
        self.matched_driver_list=[]
        self.ride=None
        self.ride_requested=False
        Pathao.add_passenger(self)

    
    def ride_request(self,destination,vehicle):
        self.destination=destination
        self.vehicle_type=vehicle
        self.ride_requested=True
        Operations.ride_match(self)
    
    def end_ride(self,ride):
        ride.stop_ride()
    
    
    

class Driver(User):
    def __init__(self, name, curr_loc, mail, password,vehicle_type,vehicle_color):
        super().__init__(name, curr_loc, mail, password)
        self.vehicle=Vehicle(vehicle_type,vehicle_color)
        self.in_active_ride=False
        self.ride_requests=[]
        Pathao.add_driver(self)
    

    def ride_accept(self,passenger):
        return Ride(self,passenger)
    

    def ride_start(self,ride):
        ride.start_ride()
        