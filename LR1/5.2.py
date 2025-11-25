print("Вхідні дані:")
print("apple banana pear")
print("pear orange mango")
print("Вихідні дані:")

set1 = {"apple", "banana", "pear"}
set2 = {"pear", "orange", "mango"}
print(*set1.intersection(set2))