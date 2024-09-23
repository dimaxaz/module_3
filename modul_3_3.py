def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()                          # Все параметры по умолчанию
print_params(25)                        # Изменяем только (a)
print_params(b='новая строка')          # Изменяем только (b)
print_params(c=[1, 2, 3])               # Изменяем только (c)

values_list = [42, 'пример', False]
values_dict = {'a': 3.14, 'b': 'тест', 'c': None}

print("Распаковка из списка:")
print_params(*values_list)              # Используем распаковку из списка

print("Распаковка из словаря:")
print_params(**values_dict)             # Используем распаковку из словаря

values_list_2 = [54.32, 'Строка']
print("\nРаспаковка с отдельными параметрами:")
print_params(*values_list_2, 42)     # Используем распаковку и передаем значение для (a)