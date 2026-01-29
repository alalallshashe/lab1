# Чтение двух целых чисел из ввода
a = int(input().strip())
b = int(input().strip())

# Сравнение чисел
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("equal")