print("=== Задача 383 ===")
ch = input("Введіть символ для побудови літери A: ")

print("Вивід:")
print(" " + ch*3)
for _ in range(2):
    print(ch + "   " + ch)
print(ch*5)
for _ in range(3):
    print(ch + "   " + ch)