from pathao import Pathao
from operations import Operations
import time

class Ride:
    def __init__(self,driver,passenger):
        self.driver=driver
        self.passenger=passenger
        self.fare=Operations.calculate_fare(passenger.curr_loc,passenger.destination)
        Pathao.list_rides.append(self)
        


    def start_ride(self):
        print()
        print("*"*8,"Ride Started","*"*8)
        print()
        self.passenger.ride_requested=False
        self.driver.in_active_ride=True
        self.passenger.ride=self
        self.driver.ride_requests.clear()
        self.passenger.matched_driver_list.clear()
        
    def stop_ride(self):
        self.driver.in_active_ride=False
        self.driver.curr_loc=self.passenger.destination
        self.passenger.curr_loc=self.passenger.destination
        self.passenger.ride=None
        print()
        print("*"*8,"Ride Ended","*"*8)
        print()
        