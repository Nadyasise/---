print("Введіть послідовність цілих чисел (через пробіл):")
nums = list(map(int, input().split()))
squares = [x**2 for x in nums]
print("Вихідні дані:")
print(*squares)