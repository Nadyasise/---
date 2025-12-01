from datetime import date

print("Введіть рік народження:")
y = int(input())
print("Введіть місяць народження:")
m = int(input())
print("Введіть день народження:")
d = int(input())

today = date.today()
birth = date(y, m, d)

age = today.year - birth.year
if (today.month, today.day) < (m, d):
    age -= 1

print("Вихідні дані:")
print(age)