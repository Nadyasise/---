def in_circle(x, y, xc, yc, r):
    print(("NO", "YES")[(x - xc)**2 + (y - yc)**2 <= r**2])

print("Ввід:")
x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
xc = float(input("Введіть xc (центр по x): "))
yc = float(input("Введіть yc (центр по y): "))
r = float(input("Введіть r (радіус): "))

print("Вивід:")
in_circle(x, y, xc, yc, r)