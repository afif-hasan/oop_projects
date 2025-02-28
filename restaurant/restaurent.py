from menu import Menu

class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} with email {employee.email} is added!!")
        print()
    def view_employee(self):
        print("      ******employee list******")
        print("name\tmail\t\tphone\tDesig.\tAddress")
        for emp in self.employees:
            print(f"{emp.name} {emp.email} \t{emp.phone}   {emp.designation}   {emp.address} ")
        print()
  