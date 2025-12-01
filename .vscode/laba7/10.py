D = {'a': 0, 'b': 1, 'c': 2}

# Всі ключі словника
keys = D.keys()
print(keys)
for key, value in D.items():
    if value == 1:
        print(key)