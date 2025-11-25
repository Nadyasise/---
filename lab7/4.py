def min2(a, b):
    return a if a < b else b

def min3(a, b, c):
    return min2(min2(a, b), c)

print("Ввід:")
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

print("Вивід:")
print(min3(a, b, c))