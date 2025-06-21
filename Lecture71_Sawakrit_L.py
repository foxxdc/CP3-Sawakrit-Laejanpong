menuList = []
priceList = []
totalPrice = 0

while True:
    menuInput = input("Menu (type 'exit' to finish): ")
    if menuInput.lower() == "exit":
        break
    priceInput = input("Price: ")
    try:
        price = int(priceInput)
    except ValueError:
        print("Please enter a valid number for price.")
        continue

    menuList.append(menuInput)
    priceList.append(price)
    totalPrice += price


def showBill():
    print("\n----- Bill -----")
    for i in range(len(menuList)):
        print(f"{menuList[i]} -> {priceList[i]} THB")
    print("----------------")
    print(f"Total: {totalPrice} THB")


showBill()
