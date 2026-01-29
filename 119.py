# Чтение ввода
sentence = input().strip()
target = input().strip()
replacement = input().strip()

# Простая замена всех вхождений
# В Python replace() по умолчанию заменяет все вхождения
result = sentence.replace(target, replacement)

# Вывод результата
print(result)

