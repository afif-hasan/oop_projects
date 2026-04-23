class Pathao:
    # list_users=[]
    list_passengers=[]
    list_drivers=[]
    list_rides=[]
    list_places=["Uttara","Airport","Banani","Mohakhali","Farmgate","New Market","College Gate"]

    @classmethod
    def add_passenger(cls,passenger):
        cls.list_passengers.append(passenger)
        print("\nNew Passenger added !!!!\n")
    
    @classmethod
    def add_driver(cls,driver):
        cls.list_drivers.append(driver)
        print("\nNew Driver added !!!!\n")
