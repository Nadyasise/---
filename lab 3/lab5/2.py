print("Введіть один або кілька рядків списків чисел:")
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    nums = list(map(int, line.split()))
    nums = [nums[-1]] + nums[:-1]
    print("Вихідні дані:")
    print(*nums)