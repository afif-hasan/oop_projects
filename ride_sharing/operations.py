# from users import Passenger,Driver
from pathao import Pathao


class Operations:

    @staticmethod
    def ride_match(passenger):
        # matched_driver_list=[]
        if len(Pathao.list_drivers)==0:
            print()
            print(" No driver to show !!!")
            print()
        else:
            for driver in Pathao.list_drivers:
                if (driver.curr_loc==passenger.curr_loc) and (driver.in_active_ride==False) and (driver.vehicle.type==passenger.vehicle_type):
                    passenger.matched_driver_list.append(driver)
        
            if len(passenger.matched_driver_list)==0:
                print("No driver matched !!!")
            else: 
                fare=Operations.calculate_fare(passenger.curr_loc,passenger.destination)
                print("Here are the ride options: ")
                for i in range(len(passenger.matched_driver_list)):
                    print(i+1,passenger.matched_driver_list[i].name,f"{passenger.matched_driver_list[i].vehicle.color} color")
                print(f"Total Fare: {fare}")
                option=int(input("Option: "))
                choosen_driver=passenger.matched_driver_list[option-1]
                choosen_driver.ride_requests.append(passenger)

        


    
    @staticmethod
    def calculate_fare(frm,to):
        start=Pathao.list_places.index(frm.title())
        stop=Pathao.list_places.index(to.title())
        return abs(start-stop)*100


