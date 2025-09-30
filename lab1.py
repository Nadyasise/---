
# Reed data (three examples of conditions)
n1 = float(input("введіть суму розрахунку №1: "))
n2 = float(input("введіть суму розрахунку №2: "))
n3 = float(input("введіть суму розрахунку №3: "))

# Calculation for each bill
p1 = (n1 * 1.10) / 3
p2 = (n2 * 1.10) / 3
p3 = (n3 * 1.10) / 3

# Output results (rounding to 2 decimal places)
print(f"Кожен друг повинен заплатити за рахунок №1: {p1:.2f} грн")
print(f"Кожен друг повинен заплатити за рахунок №2: {p2:.2f} грн")
print(f"Кожен друг повинен заплатити за рахунок №3: {p3:.2f} грн")