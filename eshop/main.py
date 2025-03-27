from shop import Shop
from product import Product
from person import Person,Seller,Customer

swapna=Shop('swapna','Trishal')

def seller_menu(seller):
    while True:
        print()
        print("------Welcome to Dashboard----------")
        print("1.Add Products")
        print("2.View Products")
        print("3.Logout")
        choice=input("Enter your choice: ")
        if choice=='1':
            nm=input("Enter product name: ")
            price=int(input("Enter unit price: "))
            quantity=int(input("Enter quantity: "))
            # product=Product(nm,price)
            seller.add_products(nm,price,quantity,swapna)
            print()
        elif choice=='2':
            seller.view_products(swapna)
        elif choice=='3':
            break
        else:
            print()
            print("#######  Invalid Input  #######")

def customer_menu(customer):
    while True:
        print()
        print("--------Welcome to Swapna-------")
        print("1.View Products")
        print("2.Buy products")
        print("3.Logout")
        choice=input("Enter your choice: ")
        if choice=='1':
            customer.view_products(swapna)
        elif choice=='2':
            nm=input("Enter product name: ")
            quantity=int(input("Enter the quantity: "))
            customer.buy_product(nm,quantity,swapna)
        elif choice=='3':
            break
        else:
            print()
            print("#######  Invalid Input  #######")

def seller_login():
    print()
    print("-------Seller Login----------")
    print()
    mail=input("Enter your mail: ")
    passwrd=input("Enter your password: ")
    if swapna.authenticate_seller(mail,passwrd)==True:
        seller=swapna.sellers[mail]
        seller_menu(seller) #seller menu 
    else:
        print("")
        print("!!!!!!! Authentication Error !!!!!!!!")
        print()

def customer_login():
    print()
    print("-----Customer Login-------")
    print()
    mail=input("Enter your mail: ")
    passwrd=input("Enter your password: ")
    if swapna.authenticate_customer(mail,passwrd)==True:
        customer=swapna.customers[mail]
        customer_menu(customer) #customer menu
    else:
        print("")
        print("!!!!!!! Authentication Error !!!!!!!!")
        print()

def seller_signup():
    print("------Seller Sign Up---------")
    print()
    mail=input("Enter your email: ")
    passwrd=input("Enter your password: ")
    seller1=Seller(mail,passwrd)
    swapna.add_sellers(seller1)
    print()
    print("Seller account added successfully !!!!!!!!!!!!")

def customer_signup():
    print("------Customer Sign Up---------")
    print()
    mail=input("Enter your email: ")
    passwrd=input("Enter your password: ")
    customer1=Customer(mail,passwrd)
    swapna.add_customers(customer1)
    print()
    print("Customer account added successfully!!!!!!!!!")

# HOMEPAGE STARTS        
while True:
    print()
    print("------Home-------")
    print("press 1 to sign up")
    print("press 2 to login")
    print("press 3 to exit")
    choice=input("Enter your choice: ")
    #home choice
    if choice=='1':
        while True:
            print()
            print("---------Sign Up interface---------")
            print()
            print("1.Customer sign up")
            print("2.Seller sign up")
            print("3.Homepage")
            choice=input("Enter your choice: ")
            #sign up choice
            if choice=='1':
                print()
                customer_signup()
                print("")
                break
            #signup choice
            elif choice=='2':
                print()
                seller_signup()
                print("")
                break
            #signup choice
            elif choice=='3':
                break # goes to home
            else:
                print()
                print("#######  Invalid Input  #######")

    #home choice:
    elif choice=='2':
        while True:
            print()
            print("------Login Interface-------")
            print()
            print("1.Customer login")
            print("2.Seller login")
            print("3.Homepage")
            choice=input("Enter your choice: ")
            #login choice
            if choice=='1':
                customer_login()
            elif choice=='2':
                seller_login()
            elif choice=='3':
                break
            else:
                print()
                print("#######  Invalid Input  #######")
        
    #home choice
    elif choice=='3':
        break #out of the code

    else:
        print()
        print("#######  Invalid Input  #######")