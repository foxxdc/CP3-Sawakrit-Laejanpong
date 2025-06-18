def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = float(input("How much is this is? : "))
print(vatCalculate(price))
