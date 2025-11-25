print("Вхідні дані:")
print("200")
print("Вихідні дані:")

stocks = {"AMZN": 130.55, 
          "GOOG": 290.40, 
          "TSLA": 180.00, 
          "MSFT": 400.10}
n = 200
for k, v in stocks.items():
    if v > n:
        print(k, v)
