print("Вхідні дані:")

# Input birth year and month
birth_year = int(input("Введіть рік народження: "))
birth_month = int(input("Введіть місяць народження (1-12): "))

# Input current year and month
current_year = int(input("Введіть поточний рік: "))
current_month = int(input("Введіть поточний місяць (1-12): "))

print("Вихідні дані:")

# Calculate age
age = current_year - birth_year
if current_month < birth_month:
    age -= 1

print(age)