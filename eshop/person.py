from product import Product

class Person:
    def __init__(self,email,password):
        self.__email=email
        self.__password=password
    
    @property
    def mail(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    def view_products(self,shop):
        if len(shop.products) !=0:
            print("Name\t Price\t Quantity")
            for product in shop.products:
                print(product.name,product.price,product.quantity)
        else:
            print()
            print("No products to show!!!!!!!!!!!")

class Seller(Person):
    def __init__(self,email, password):
        super().__init__(email, password)
    
    def add_products(self,name,price,quantity,shop):
        nm=name.lower()
        fnd=False
        for product in shop.products:
            if product.name==nm:
                fnd=True
                product.quantity+=quantity
                print("Product added successfully!!!!")
                break
        if fnd==False:
            pr=Product(nm,price)
            pr.quantity=quantity
            shop.products.append(pr)
            print("Product added successfully!!!!")

class Customer(Person):
    def __init__(self,email, password):
        super().__init__(email, password)
    
    def buy_product(self,pr_name,quantity,shop):
        product_name=pr_name.lower()
        pr_fnd=False
        if len(shop.products)!=0:
            for product in shop.products:
                if product.name==product_name:
                    pr_fnd=True
                    if quantity<=product.quantity and quantity>0:
                        print(f"{quantity} {product_name} purchased")
                        print(f"Pay Tk {product.price * quantity}")
                        product.quantity-=quantity
                    else:
                        print("Invalid product quantity")
            if pr_fnd==False:
                print("Invalid Product Name")
        else:
            print()
            print("No products in the shop!!!!!!!!!!")

