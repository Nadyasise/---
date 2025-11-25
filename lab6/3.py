print("Вхідні дані:")
print("Немає")
print("Вихідні дані:")

stocks = {
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
    "ACME": 45.23
}

for key, value in sorted(stocks.items(), key=lambda x: x[1]):
    print(f"{value} {key}")