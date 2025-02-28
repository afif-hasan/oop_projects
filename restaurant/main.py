from user import Admin,Customer,Employee
from order import Order
from item import Item
from menu import Menu
from restaurent import Restaurent

lira_banu=Restaurent("lira Banur restaurent")
def customer_menu():
    name=input("Enter your name: ")
    email=input("enter your mail: ")
    phone=input("Enter your phone number:")
    address=input("enter your address: ")
    customer=Customer(name,email,phone,address)

    while True:
        print(f"*****Welcome {customer.name}*********")
        print("1.View menu")
        print("2.Add item to cart")
        print("3.View cart")
        print("4.Pay Bill")
        print("5.Exit")
        choice=int(input(("Enter your choice:")))
        if choice==1:
            customer.view_menu(lira_banu)
        elif choice==2:
            item_nm=input("Enter item name: ")
            item_qn=int(input("Enter item quantity: "))
            customer.add_to_cart(lira_banu,item_nm,item_qn)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print()
            print("****Invalid Input*****")


def admin_menu():
    name=input("Enter your name: ")
    email=input("enter your mail: ")
    phone=input("Enter your phone number:")
    address=input("enter your address: ")
    admin=Admin(name,email,phone,address)

    while True:
        print(f"*****Welcome {admin.name}*********")
        print("1.Add new item")
        print("2.Add new employee")
        print("3.View employee")
        print("4.View items")
        print("5.Delete item")
        print("6.Exit")
        choice=int(input(("Enter your choice:")))
        if choice==1:
            itm_nm=input("Enter item name: ")
            itm_price=int(input("Enter item price: "))
            itm_avail_qn=int(input("Enter available quantity: "))
            item=Item(itm_nm,itm_price,itm_avail_qn)
            admin.add_item(lira_banu,item)
        elif choice==2:
            name=input("Enter new employee name: ")
            email=input("Enter email address: ")
            phone=input("Enter phone number: ")
            address=input("Enter present address: ")
            age=input("Enter employee age: ")
            designation=input("Enter designation: ")
            salary=input("Enter salary: ")
            employee=Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(lira_banu,employee)
        elif choice==3:
            admin.view_employee(lira_banu)
        elif choice==4:
            admin.view_menu(lira_banu)
        elif choice==5:
            item_name=input("Enter item name: ")
            admin.delete_item(item_name,lira_banu)
        elif choice==6:
            break
        else:
            print()
            print("****Invalid Input*****")

while True:
    print("*****WELCOME******")
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        admin_menu()
    elif choice==2:
        customer_menu()
    elif choice==3:
        break
    else:
        print("Invalid input")
    