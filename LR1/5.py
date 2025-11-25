print("Вхідні дані:")
print("Red Green Orange White")
print("Black Green White Pink")
print("Вихідні дані:")

set1 = {"Red", "Green", "Orange", "White"}
set2 = {"Black", "Green", "White", "Pink"}

print(*set1.intersection(set2))