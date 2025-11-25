print("Вхідні дані:")
print("Немає")
print("Вихідні дані:")

games = {
    "horror": "Resident Evil",
    "strategy": "Civilization VI",
    "arcade": "Pac-Man",
    "puzzle": "Tetris",
    "rpg": "The Witcher 3"
}

for g, n in games.items():
    print(f"{g}: {n}")