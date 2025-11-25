def calc(a, b, op):
    if op == '+':
        return f"{a + b:.2f}"
    elif op == '-':
        return f"{a - b:.2f}"
    elif op == '*':
        return f"{a * b:.2f}"
    elif op == '/':
        return f"{a / b:.2f}"
    else:
        return "Unknown operation"


print("Ввід:")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+ - * /): ")

print("Вивід:")
print(calc(a, b, operation))