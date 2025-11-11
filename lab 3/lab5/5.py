print("Введіть три чотиризначні числа (кожне з нового рядка):")
numbers = [input() for _ in range(3)]

print("Вихідні дані:")
for num in numbers:
    digits = list(num)
    # Мінімальне число
    min_digits = sorted(digits)
    # якщо перша цифра 0, міняємо її з першим ненульовим елементом
    if min_digits[0] == '0':
        for i in range(1, len(min_digits)):
            if min_digits[i] != '0':
                min_digits[0], min_digits[i] = min_digits[i], min_digits[0]
                break
    min_num = ''.join(min_digits)
    
    # Максимальне число
    max_num = ''.join(sorted(digits, reverse=True))
    
    print(min_num, max_num)