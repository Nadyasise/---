print("Ввід:")
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

while b != 0:
    a, b = b, a % b
    
print("Вивід:")
print("НСД =", a)