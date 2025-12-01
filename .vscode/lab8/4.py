import random

with open("input.txt") as f:
    words = f.read().splitlines()

k = random.randint(1, len(words))
sample = random.sample(words, k)

print("Вихідні дані:")
for w in sample:
    print(w)