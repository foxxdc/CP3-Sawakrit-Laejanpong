class Vehicle:
    def __init__(self, licenseCode="", serialCode=""):
        self.licenseCode = licenseCode
        self.serialCode = serialCode

    def turnOnAirConditioner(self):
        print(f"{self.__class__.__name__} - Air Conditioner: ON")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
    def __init__(self, licenseCode="", serialCode="", color=""):
        super().__init__(licenseCode, serialCode)
        self.color = color

    def showColor(self):
        print(f"Pickup Color: {self.color}")

class Van(Vehicle):
    pass

car1 = Car("ABC123", "C001")
car1.turnOnAirConditioner()
pickup1 = Pickup("DEF456", "P001", "Red")
pickup1.turnOnAirConditioner()
pickup1.showColor()
van1 = Van("XYZ789", "V001")
van1.turnOnAirConditioner()
