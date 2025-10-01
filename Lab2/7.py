print("Вхідні дані:")

# Input chocolate dimensions and desired piece size
n = int(input("Введіть n: "))
m = int(input("Введіть m: "))
k = int(input("Введіть k: "))

print("Вихідні дані:")

# Check if it's possible to break off k pieces
if (k % n == 0 and k <= n * m) or (k % m == 0 and k <= n * m):
    print("Yes")
else:
    print("No")