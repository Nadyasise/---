import random

with open("input.txt") as f:
    lines = f.read().splitlines()

print("Вихідні дані:")
print(random.choice(lines))