t = float(input("Введіть температуру (°C): "))

print("\n--- Результат ---")
if t <= 0:
    print("A cold, isn't it?")
elif t < 10:
    print("Cool.")
else:
    print("Nice weather we're having.")
print("===================\n")