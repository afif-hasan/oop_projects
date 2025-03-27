class Shop:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.products=[] 
        self.sellers={} #{'mail':object}
        self.customers={} #{'mail':object}
 
    def add_sellers(self,seller):
        self.sellers[seller.mail]=seller
    def add_customers(self,customer):
        self.customers[customer.mail]=customer
    
    def authenticate_seller(self,mail,password):
        mail_fnd=False
        for key in self.sellers.keys():
            if key==mail:
                mail_fnd=True
                break
        if mail_fnd==False:
            print()
            print("Invalid Email Address!!!!!!!")
        else:
            slr=self.sellers[mail] #putting seller object in slr
            if slr.password==password:
                return True
            else:
                return False
       
    def authenticate_customer(self,mail,password):
        mail_fnd=False
        for key in self.customers.keys():
            if key==mail:
                mail_fnd=True
                break
        if mail_fnd==False:
            print()
            print("Invalid Email Address!!!!!!!")
        else:
            cstmr=self.customers[mail] #putting customer object in cstmr 
            if cstmr.password==password:
                return True
            else:
                return False
        
    
