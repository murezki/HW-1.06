slova = input("Введите два слова, разделенных пробелом: ")

# Разделение строки на слова
words = slova.split()

if len(words) == 2:
    reversed_string = words[1] + " " + words[0]
    print(reversed_string)
else:
    print("ERROR")