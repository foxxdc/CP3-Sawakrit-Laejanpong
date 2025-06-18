def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "BBB" and password == "BBB":
        return menu()
    else:
        return print("try again!")

def menu():
    print("Welcome! Choose one")
    print("1. Vat calculater")
    print("2. Price calculator")
    return choose()

def choose():
    userSelected = int(input(">> "))

    if userSelected == 1:
        return vatCalculate(totalPrice = int(input("Cost of goods: ")))

    elif userSelected == 2:
        return priceCalculate()

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print("Price + Vat:",result,"DOLLARs")

def priceCalculate():
    firstPiece = int(input("1stPrice : "))
    secondPiece = int(input("2ndPrice : "))
    totalPrice = firstPiece + secondPiece
    return vatCalculate(totalPrice)
login()
