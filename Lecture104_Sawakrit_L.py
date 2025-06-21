class Customer:
    def __init__(self, name, lastname, age=0):
        self.name = name
        self.lastname = lastname
        self.age = age

    def addcart(self):
        print("Added product to {self.name} {self.lastname}'s cart")
customer1 = Customer("Rodtank", "Bombbombtumtum")
customer1.addcart()
customer2 = Customer("Sawakrit", "Laejanpong")
customer2.addcart()
customer3 = Customer("Chichi", "Chongchong")
customer3.addcart()
customer4 = Customer("Kirati", "Soynid")
customer4.addcart()
