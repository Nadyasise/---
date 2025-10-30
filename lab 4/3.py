print("Введіть 3 рядки (складаються з 0 і 1):")

lines = [input(f"Рядок {i+1}: ") for i in range(3)]

print("\n Вивід:")
for s in lines:
    max_zeros = max(len(group) for group in s.split('1'))
    print(max_zeros)