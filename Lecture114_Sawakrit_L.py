from currency_converter import CurrencyConverter

c = CurrencyConverter()
item_price = {
    'USD': ('Big Mac', 6.00),
    'THB': ('ชาไทยเย็น', 35.00),
    'JPY': ('ซูชิชิ้นเล็ก', 120.00),
    'EUR': ('Espresso', 3.00),
    'GBP': ('Fish & Chips', 7.50),
    'AUD': ('Meat Pie', 5.50),
    'KRW': ('ต็อกบกกี', 4500.00)
}

amount = float(input("💵 Enter the amount of money you have: "))
from_cur = input("From currency (e.g. GBP): ").upper()
to_cur = input("Convert to currency (e.g. JPY): ").upper()

try:

    rate = c.convert(1, from_cur, to_cur)
    result = c.convert(amount, from_cur, to_cur)

    print(f"\n🔁 Exchange Rate: 1 {from_cur} ≈ {rate:.4f} {to_cur}")
    print(f"✅ {amount} {from_cur} ≈ {result:.2f} {to_cur}")

    if to_cur in item_price:
        item_name, item_cost = item_price[to_cur]
        quantity = int(result // item_cost)
        print(f"\n🛒 You can buy approximately {quantity} x '{item_name}' (Avg. price: {item_cost} {to_cur} each)")
    else:
        print(f"\n⚠️ No item price data available for {to_cur}")
except Exception as e:
    print("❌ Error:", e)
    
