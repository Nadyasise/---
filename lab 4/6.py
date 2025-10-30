print("Введіть 3 числа (рядки цифр без пробілів):")

nums = [input(f"n{i+1}: ") for i in range(3)]

print("\n Вивід:")
for num in nums:
    parts = []
    while len(num) > 3:
        parts.insert(0, num[-3:])
        num = num[:-3]
    parts.insert(0, num)
    print(",".join(parts))