
print("Введіть 3 натуральні числа (кожне з нового рядка):")

numbers = [input("n{}: ".format(i + 1)) for i in range(3)]

print("\n Вивід:")
for n in numbers:
    print(n[::-1])