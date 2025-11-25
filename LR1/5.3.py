print("Вхідні дані:")
print("cat dog mouse")
print("dog bird mouse")
print("Вихідні дані:")

set1 = {"cat", "dog", "mouse"}
set2 = {"dog", "bird", "mouse"}
print(*set1.intersection(set2))