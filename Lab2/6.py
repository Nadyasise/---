print("Вхідні дані:")

# Input three four-digit numbers
num1 = input("Введіть число 1: ")
num2 = input("Введіть число 2: ")
num3 = input("Введіть число 3: ")

numbers = [num1, num2, num3]

print("Вихідні дані:")

# Check if sum of first two digits equals sum of last two digits
for num in numbers:
    first_sum = int(num[0]) + int(num[1])
    last_sum = int(num[2]) + int(num[3])
    print(first_sum == last_sum)