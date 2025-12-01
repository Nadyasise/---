album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set3 = set(["Thriller", "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Варіант 1: через метод issubset()
print(album_set1.issubset(album_set3))

# Варіант 2: через оператор <=
# print(album_set1 <= album_set3)