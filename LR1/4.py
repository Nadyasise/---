print("Вхідні дані:")
print("200")
print("Вихідні дані:")

stocks = {
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
    "ACME": 45.23
}

n = 200
for k, v in stocks.items():
    if v > n:
        print(k, v)