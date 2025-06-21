menuDict = {
    'fried rice': 65,
    'burger': 45,
    'spaghetti': 99,
    'noodle': 55,
    'salad': 60 #why its hella expensive bruh
}

menuList = []
total = 0

print(menuDict)

while True:
    menuInput = input("MENU (type 'exit' to finish): ").lower()
    if menuInput == "exit":
        break
    elif menuInput in menuDict:
        price = menuDict[menuInput]
        menuList.append([menuInput, price])
        total += price
    else:
        print("Menu not found. Please choose from the listed menu.")

def showBill():
    print('----- Bill -----')
    for item in menuList:
        print("{item[0]} -> {item[1]} THB")
    print("----------------")
    print("Total price: {total} THB")

showBill()
