print("Вхідні дані:")
print("300")
print("Вихідні дані:")

stocks = {"NVDA": 480.20, 
          "META": 330.40, 
          "XOM": 120.55}
n = 300
for k, v in stocks.items():
    if v > n:
        print(k, v)