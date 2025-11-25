print("Вхідні дані:")
print("Немає")
print("Вихідні дані:")

stocks = {"TSLA": 190.40, "AMZN": 112.55,
           "GOOG": 2800.90, "MSFT": 320.10}

for k, v in sorted(stocks.items(), key=lambda x: x[1]):
    print(f"{v} {k}")