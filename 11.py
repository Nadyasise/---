
birth_year = int(input())
birth_month = int(input())
current_year = int(input())
current_month = int(input())
age = current_year - birth_year
if current_month < birth_month:
    age -= 1
# Якщо month рівні, то повний рік вже пройшов, тому корекції не потрібно
print(age)