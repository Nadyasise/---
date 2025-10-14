print("Ввід:")
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

# Ініціалізація
quotient = 0
remainder = a

# Обчислюємо ділення через віднімання
while remainder >= b:
    remainder -= b
    quotient += 1

print("Вивід:")
print("Результат:", quotient, remainder)