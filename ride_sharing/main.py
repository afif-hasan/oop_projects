from pathao import Pathao
from users import Passenger,Driver
# from vehicle import Vehicle


def sign_up():
    print("\nSign up as:")
    print("1. Passenger")
    print("2. Driver")
    op=int(input("Option: "))
    if op==1:
        print()
        print("*"*5,"WELCOME","*"*5)
        nm=input("Your Name: ")
        print("Choose your current location: ")
        for location in Pathao.list_places:
            print(location)
        loc=input("Location: ").title()
        email=input("Your email: ").lower()
        password=input("Type your password: ")
        p=Passenger(nm,loc,email,password)
        return p
    else:
        print()
        print("*"*5,"WELCOME","*"*5)
        nm=input("Your Name: ")
        print("Choose your current location: ")
        for location in Pathao.list_places:
            print(location)
        loc=input("Location: ").title()
        print("Do you have car or bike? ")
        print("1. Car \n2.Bike")
        vehicle_type=int(input("Option: "))
        vehicle_color=input("Color: ").title()
        v_type=None
        if vehicle_type==1:
            v_type="Car"
        else:
            v_type="Bike"
        email=input("Your email: ").lower()
        password=input("Type your password: ")
        d=Driver(nm,loc,email,password,v_type,vehicle_color)
        return d


def login():
    print("Login as:\n1.Passenger\n2.Driver")
    option=input("option: ")
    if option=="1":
        email=input("Enter your mail: ")
        password=input("Enter you password: ")
        for user in Pathao.list_passengers:
            if user.mail==email:
                if user.password==password:
                    print()
                    print("Successfully Logged In !!!")
                    print()
                    return user
                else:
                    return "wrong_pass"
            else:
                print()
                print("Invalid Email address !!!")
    elif option=="2":
        email=input("Enter your mail: ")
        password=input("Enter you password: ")
        for user in Pathao.list_drivers:
            if user.mail==email:
                if user.password==password:
                    print()
                    print("Successfully Logged In !!!")
                    print()
                    return user
                else:
                    return "wrong_pass"
            else:
                print()
                print("Invalid Email address !!!")
    else:
        return 1


def book_ride(user):
    print("Choose destination: ")
    for location in Pathao.list_places:
        if user.curr_loc!=location:
            print(location)
    destiny=input("Location: ").title()
    print("Choose a vehicle:")
    print("1. Car\n2.Bike")
    option=int(input("Option: "))
    v=None
    if option==1:
        v="Car"
    else:
        v="Bike"
    user.ride_request(destiny,v)


def  passenger_options(user):
    while True:
        print(f"Your Location: {user.curr_loc}")
        print("Choose Options: ")
        if user.ride==None:
            print("1.Request a ride")
            print("2.Logout")
            option=int(input("Option: "))
            if option==1:
                book_ride(user)
            else:
                break
        else:
            print("1.Stop current ride")
            print("2.Logout")
            option=int(input("Option: "))
            if option==1:
                user.end_ride(user.ride)
            else:
                break


def driver_options(user):
    while True:
        print(f"Your Location: {user.curr_loc}")
        print("Choose options: ")
        if user.in_active_ride:
            print("******** In active ride right now ********")
            print("1.Logout")
            option=int(input("Option: "))
            if option==1:
                break
        else:
            print("1.Ride requests nearby")
            print("2.Logout")
            option=int(input("Option: "))
            if option==1:
                if len(user.ride_requests)==0:
                    print()
                    print("No nearby rides !!!")
                    print()
                else:
                    for i in range(len(user.ride_requests)):
                        print(i+1,user.ride_requests[i].name,f"Destination at {user.ride_requests[i].destination}")
                    option=int(input("Choose to start ride: "))
                    choosen_passenger=user.ride_requests[option-1]
                    ride=user.ride_accept(choosen_passenger)
                    user.ride_start(ride)
            else:
                break


while True:
    user=None
    print("*"*8,"Welcome to Pathao","*"*8)
    print("Choose the option: \n1. Sign up\n2. Login")
    option=input("Option: ")
    if option=="1":
        sign_up()
    elif option=="2":
        user=login()
        if user == 1:
            print()
            print(" Invalid option !!!")
            print()
        elif user == None:
            print()
            print(" No such user found !!!")
            print()
        elif user=="wrong_pass":
            print()
            print("Wrong Password !!!")
            print()
        else:
            if isinstance(user,Passenger):
                passenger_options(user)
            else:
                driver_options(user)            
    else:
        print("Invalid option!!!")