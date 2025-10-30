text = input("Введіть рядок: ")
ch = input("Введіть символ: ")

first = text.find(ch)
last = text.rfind(ch)

if first != -1 and last != -1 and first != last:
    middle = text[first+1:last][::-1]
    new_text = text[:first+1] + middle + text[last:]
    print("Вивід:", new_text)
else:
    print("Символ зустрічається менше двох разів.")