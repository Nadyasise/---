print("Вхідні дані:")
t1 = float(input("введіть значення температур "))
t2 = float(input("введіть значення температур "))
t3 = float(input("введіть значення температур "))

print("Вихідні дані:")

for t in [t1, t2, t3]:
    if t <= 0:
        print("A cold, isn't it?")
    elif t < 10:
        print("Cool.")
    else:
        print("Nice weather we're having.")