class Menu:
    def __init__(self):
        self.item_list=[]

    def add_item(self,item):
        self.item_list.append(item)
        print(f"{item.name} quantity: {item.avail_quantity} is added to menu")

    def find_item(self,item_name):
        for item in self.item_list:
            if item.name.lower()==item_name.lower():
                return item
        return None
    def delete_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.item_list.remove(item)
            print(f"{item.name} is removed from MENU!!!")
            print()
        else:
            print('Item not found on menu!!!!')
            print()
    def view_menu(self):
        print("   ******MENU******")
        print("name\tprice\tquantity")
        for item in self.item_list:
            print(f"{item.name}\t{item.price}\t{item.avail_quantity}")
        print()
