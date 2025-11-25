print("Вхідні дані:")
print("Немає")
print("Вихідні дані:")

stocks = {"XOM": 104.88, "NVDA": 469.77, "META": 335.00}

for k, v in sorted(stocks.items(), key=lambda x: x[1]):
    print(f"{v} {k}")