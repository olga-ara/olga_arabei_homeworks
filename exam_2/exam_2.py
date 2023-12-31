# 1. Как изменить значение элемента списка?
# list1 = [1, 2, 3]
# list1[0] = 66
# print(list1)

# 2. Что выведет данный код?
# a = [1, 3]
# print(int(a))
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

# 3. Что выведет данный код?
# a = str([1, 1])
# print(a)
# список [1, 1]

# 4.Что выведет данный код?
# a = [2, 4, 8]
# print(a[::-2])
# [8, 2]

# 5. Как объединить два списка?
# сложение списков
# list1 = [1, 2, 3, 4, 5]
# list2 = [9, 8, 7, 6, 5]
# new_list = list1 + list2
# print(new_list)
# или при помощи расширения списка
# list1.extend(list2)
# print(list1)

# 6. Как отсортировать список в порядке убывания?
# list3 = [1, 2, 3, 4, 5, 6]
# # метод реверс
# list3.reverse()
# print(list3)
# # или
# list3.sort(reverse=True)
# print(list3)

# 7. Как объединить два кортежа?
# tuple2 = (1, 2, 3, 4, 5)
# tuple4 = (5, 6, 7, 8, 9)
# new_tuple = tuple4 + tuple2   # (5, 6, 7, 8, 9, 1, 2, 3, 4, 5)
# print(new_tuple)
# или расширить 1 кортеж другим
# tuple1 = (1, 2, 3)
# tuple2 = (5, 6, 7, tuple1 )
# print(tuple2)

# 8. Можно ли умножать кортеж на число?
# tuple2 = (1, 2, 3, 4, 5)
# new_tuple = tuple2 * 2
# print(new_tuple)

# 9. Что выведет данный код?
# a = list('py')
# print(len(a))
# выведет 2 (длина строки)

# 10. Что выведет данный код?
# a = [2, 4, 8]
# print(a[::4])
# выведет 2

# 11. Как добавить элемент в словарь?
# dict[key] = value
# update({key:value, key2:value})
# my_dict = {1: 10, 2: 20}
# my_dict[3] = 30
# print(my_dict)
# или методом update
# my_dict.update({4: 40, 5: 50})
# print(my_dict)

# 12. Как получить значение элемента в словаре?
# print(dict[key])
# указать словарь и ключ
# dict1 = {'кошка': 5, 'собака': 6}
# print(dict1['кошка'])


# 13.Как удалить элемент из словаря?
# dict1 = {'кошка': 5, 'собака': 6}
# dict1.pop('кошка')
# print(dict1)
# del dict1['собака']
# print(dict1)


# 14.Что выведет данный код
# a = [1, 2]
# print(type(a))
# b = (1, 2)
# print(type(b))
# print(a == b)
# False а != b

# 15.Что выведет данный код
# a = []
# for i in range(3):
#     [] + [0], [0] + [1], [0, 1, ] + [2]
#     a += [i]
# print(a)
# список [0, 1, 2]

# 16. Что такое исключение(exception) в Python?
# Тип данных, который сообшает об ошибках

# 17. Как обработать  несколько разных исключений?
"""При помощи конструкции try – except (также инстукция  except без аргументов, 
или  except Exception, которая перехватывает все исключения, 
или несколько except-ов)"""

# 18.Какиспользовать блок finally приобработке исключений?
"""Этот блок - вывод программы в самом конце, он срабатывает 
в любом случае, независимо было выполнено исключение или нет"""

# # 19. Как открыть файл для чтения в Python?
# a. Методом open
# file = open('task_1.txt', 'r') – указать имя файла и режим открытия, при этом методе обязательно
# использование метода close (file.close())
# b. инструкция with
# with open('task_1.txt', 'r') as file:
#     print(file)

# # 20. Как прочитать содержимое файла?
# with open('file_name.txt') as file:
#     file.readlines()

# 21. Как закрыть файл после работы с ним?
# file.close()

# # 22. Что такое CSV файл?
"""- это формат файла (данных) (еxsel – таблицы), структура файла проявляется 
в разделелителе (;), CSV – comma separated values – значения разделенные запятыми"""

# 23. Как записать данные в CSV файл?
# with open('file_1.csv', 'w') as f:
#     writer = csv.writer(f)

# # 24. Что выведет данный код
# a = [1, 2]
# print(a[len(a)])  # ошибка IndexError
# print(len(a))  # - правильный вариант

# 25. Что выведет данный код
# a = (1, 2) + 2
# print(a)
# TypeError

# 26. Что выведет данный код
# a = [1, 2, 3]
# b = 0
# for i in a:
#     if a[i - 1] < 2:
#         b += a[i]
#     else:
#         b -= 1
# print(b)  # вывод 0


# #27. Что выведет данный код
# a = (1, 3)
# b = (0, 100)
# print(a > b)


# # 28. Что выведет данный код
# var = '{0}{0}'.format(1, 4)
# print(int(var))
# 11

# # 29.Что выведет данный код
# lst = [1]
# lst.extend('hi')
# lst.append('hey')
# print(lst)   # [1, 'h', 'i', 'hey']

# # 30.Что выведет данный код
# string = 'abcdefghijklmnopqrst'
# print(max(string), min(string))
# маx = t - св=амый последний элемент и самый первый
# min = a
