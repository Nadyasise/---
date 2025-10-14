print("Ввід:")
n = int(input("Введіть кількість автомобілів: "))

# Ініціалізація змінних
max_speed = 0
min_speed = 300
slow_cars = 0

# Введення швидкостей та підрахунок
for i in range(n):
    speed = int(input(f"Введіть швидкість автомобіля {i+1}: "))
    if speed > max_speed:
        max_speed = speed
    if speed < min_speed:
        min_speed = speed
    if speed <= 30:
        slow_cars += 1

print("Вивід:")
print(max_speed - min_speed)
print(slow_cars)