class Order:
    def __init__(self):
        self.items={}
    
    def add_item(self,item,quantity):
        if item in self.items:#jodi age theke thake cart e
            self.items[item]+=quantity
        else:
            self.items[item]=quantity#naile value te quantity ta rekhe dao
        item.avail_quantity-=quantity
    
    @property
    def total_price(self):
        sum=0
        for item,quantity in self.items.items():
            sum+=(item.price*quantity)
        return sum
    def clear(self):
        self.items.clear()

