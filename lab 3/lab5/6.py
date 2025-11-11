print("Введіть послідовність чисел ")
data = input().split(',')
lists = [list(map(int, part.split())) for part in data]
print("Вихідні дані (початковий список):")
print(lists)
lists.sort(key=lambda x: x[1])
print("Вихідні дані (відсортований список):")
print(lists)