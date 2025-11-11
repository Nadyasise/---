print("Введіть послідовність цілих чисел (через пробіл):")
nums = list(map(int, input().split()))
even = sorted([x for x in nums if x % 2 == 0], reverse=True)
odd = [x for x in nums if x % 2 != 0]
print("Вихідні дані:")
print(*even, *odd)