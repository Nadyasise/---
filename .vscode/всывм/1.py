# Задання довгого рядка у змінній G
G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, \
Mary went Everywhere that Mary went The lamb was sure to go"
# Замінюємо всі входження слова "Mary" на "Bob"
G_new = G.replace("Mary", "Bob")

# Виводимо результат
print(G_new)