# Чтение целого числа из ввода
number = int(input().strip())

# Проверка на четность с помощью оператора %
if number % 2 == 0:
    print("even")
else:
    print("odd")