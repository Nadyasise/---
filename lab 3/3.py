print("Ввід:")
n = int(input("Введіть число n: "))
m = int(input("Введіть число m: "))
p = int(input("Введіть число p: "))

# Функція для обчислення факторіалу
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print("Вивід:")
print(factorial(n))
print(factorial(m))
print(factorial(p))