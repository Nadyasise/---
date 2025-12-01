album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Варіант 1: через метод union()
album_set3 = album_set1.union(album_set2)

# Варіант 2: через оператор |
# album_set3 = album_set1 | album_set2

print(album_set3)