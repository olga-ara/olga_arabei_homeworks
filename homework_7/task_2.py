# Даны 2 списка:
# Выполнить следующие операции: 1)Сложить два списка
a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
new_list = a + b
print(new_list)
# 2) Добавьте элемент 6 на 3 позицию.
new_list.insert(2, 6)
print(new_list)
# 3)Удалите все текстовые переменные
new_c = []
for i in new_list:
    if type(i) != str:
        new_c.append(i)
print(f'Список без текстовых элементов: {new_c}')

# 4) Посчитайте количество элементов списка
print(len(new_c))
