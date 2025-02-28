from abc import ABC
from order import Order

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
    def view_employee(self,restaurent):
        restaurent.view_employee()
    def add_item(self,restaurent,item):
        restaurent.menu.add_item(item)
    def delete_item(self,item_name,restaurent):
        restaurent.menu.delete_item(item_name)
    def view_menu(self,restaurent):
        restaurent.menu.view_menu()

class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, email, phone, address)



class Customer(User):
    def __init__(self, name, email, phone, address):
        self.cart=Order()
        super().__init__(name, email, phone, address)

    def view_menu(self,restaurent):
        restaurent.menu.view_menu()
    
    def add_to_cart(self,restaurent,item_name,quantity):#ekhan theke shuru korbooooooo
        item=restaurent.menu.find_item(item_name)
        if item:#same as if item:
            if item.avail_quantity>=quantity:
                self.cart.add_item(item,quantity)
                print(f"{item.name} successfully added to cart!!")
            else:
                print(f"Sorry!! Only {item.avail_quantity} {item.name} are available")
        else:
            print("ITEM is not available!!!")
    def view_cart(self):
        print("*******View Cart********")
        print("name\tprice\tUnits")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print()
        print(f"Total Price: {self.cart.total_price}")

    def remove_from_cart(self,restaurent,item_name):
        item=restaurent.menu.find_item(item_name)
        if item in self.cart.items:
            del self.cart.items[item]
        else:
            print(f"{item_name} is not in cart!!!")

    def pay_bill(self):
        print(f"{self.cart.total_price}TK paid successfully!!")
        self.cart.clear()



        