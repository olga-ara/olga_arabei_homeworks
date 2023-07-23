# 1 используя стандартные арифметические операции представьте самое большое число из цифр  4  4  4
# и приведите его значение
# print(4 ** 4 ** 4)  # самое большое число это 4 в степени 256
# print(4 ** (4 ** 4))


# 2 написать программу для вычисления хначения выражений.
# проверить правильность выполнения задания с помощью тестовых значений
# import math
#
# alpha = int(input('введите значение альфа: '))
# beta = int(input('введите значение бета: '))
# gamma = int(input('введите значение гамма: '))
# y = (1 / 4) * (math.sin(alpha + beta + gamma) + math.sin(beta + gamma - alpha) +
#                math.sin(gamma + alpha - beta) - math.sin(alpha + beta + gamma))
# print(y)


# 3 Создать пустую переменную. Проверить ее на истинность и ложность.

# a = None   # любая пустая переменная будет фолс
# print(bool(a))
# # если мы имеем не пустые переменные мы получим
# x = 3  # True
# y = 0   # False
# print(bool(x), bool(y))


# 4 даны 2 целых числа m и n (m <= n). Написать прогу которая выводит все числа от m до n включительно
# m = int(input('введите первое число: '))
# n = int(input('введите второе число: '))
# for elem in range(m, n + 1):
#     print(elem)


# 5 Даны 2 целых числа m и n. Написать прогу, которая выводит все числа от m до n
# включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае
# m = int(input('введите первое число: '))
# n = int(input('введите второе число: '))
# if m < n:
#     for elem in range(m, n + 1):
#         print(elem)
# else:
#     for elem in range(m, n - 1, -1):
#         print(elem)


# 6 В строке "Иван Иванов" поменяйте местами слова
# string = 'Ольга Арабей'
# string_split = string.split(' ')
# print(f'{string_split[-1]} {string_split[0]}')
#
# # второй способ
# string_list = list(reversed(string_split))
# print(string_list)
#
# # третий способ
# string_join = " ".join(string_list)
# print(string_join)

# 7 создать список с числами от 1 до 50 использую генератор списков
# list = [i for i in range(1, 50)]
# print(list)
#
# # аналогичная запись
# x = []
# for i in range(1, 50):
#     x.append(i)
# print(x)


# 8 Вам передан массив чисел, Каждое число в этом массиве имеет пару, кроме одного
# : [1,5,2,9,2,9,1] = > 5, вывести число, которое встречается 1 раз
# my_list = [1, 5, 2, 9, 2, 9, 1]
# for i in my_list:
#     if my_list.count(i) == 1:
#         print(i)


# 9
# list_students = ['student1', 'student2', 'student3']
# for i in list_students:
#     print(i + '_good')
#
# # второй способ
# new_list = [i + '_good' for i in list_students]
# print(new_list)

# 10
# вывести на экран числа от 0 до 50 кроме 35
# for i in range(0, 50):
#     if i == 35:
#         continue
#     print(i, end=' ')

# 11 Дана строка, в новый список добавить элементы, которые содержат пробел
my_string = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_string = []
for i in my_string:
    if ' ' in i:
        new_string.append(i)
print(new_string)

# второй вариант
my_string = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_string = []
for i in my_string:
    if i.count(' '):
        new_string.append(i)
print(new_string)
# если в наших элементах есть пробел, добавить новые элементы в список


# 12 в классе N школьников, на 1 и 2 рассчитайсь!
students = int(input('ввести количество учеников: '))
for i in range(students):
    if i % 2 == 0:
        print(1)
    else:
        print(2)

# второй способ
for digit in range(students):
    if digit < students - 1:
        print(('первый', 'второй')[digit % 2])
    else:
        print(('первый', 'второй')[digit % 2] + ' расчет окончен!')


# 13 Дан список чисел, необходимо удалить все вхождения числа 20 из него
numbers = [1, 2, 3, 20, 200, 20, 20, 30]
for i in numbers:
    if i == 20:
        numbers.remove(i)
print(numbers)   #[1, 2, 3, 200, 20, 30]
# 'этот способ из-за смещения индекса работает некорректно!!!!
# что бы это избежать нужен другой способ!!!
# 2 способ
list1 = [i for i in numbers if i != 20]
print(list1)  #[1, 2, 3, 200, 30]

# способ 3
while 20 in numbers:
    numbers.remove(20)
print(numbers)   # [1, 2, 3, 200, 30]


# 14 c клавы вводится 10зн число, вывести на экран четные числа входящие в данное число
number = input('введите десятизначное число: ')
if len(number) == 10:
    for i in number:
        if int(i) % 2 == 0:
            print(i, end=' ')
else:
    print('вы ввели не десятизначное число ')

# 15 удалите пустые строки из списка строк
list1 = ['name', 'hello', '', '', 'apple']
list_new = [i for i in list1 if i != '']
print(list_new)

# 16 напишите прогу, которая вычисляет процентное содержание
# cимволов G - гуанин и С - цитозин в введенной строке (прога не должна зависеть от регистра)
# например: в строке "acggtgttat" процентное содержание символов
# G и С = 4/10*100 = 40.0 где 4 - кол-во символов G b C  а 10 - длина строки

chem_formula = input('введите химическую формулу: ').upper()
count_simb = 0  # колическтво символов
proc_simb = 0  # процентное содержание
for i in chem_formula:
    if i == 'C':
        count_simb += 1
    if i == 'G':
        count_simb += 1
    proc_simb = count_simb * 100/len(chem_formula)
print(proc_simb)


# 17 ДНК представляет собой химическое вещество , в цепочках ДНК символы А и Т
# дополняют друг друга, нужно вернуть другую дополнительную сторону. НИТЬ ДНК не бывает пустой или
# ДНК не существует
#  "ATTGC --> "TAACG"       "GTAT --> "CATA"
dna = 'ATTGC'
new_dna = ''
for i in dna:
    if i == 'A':
        new_dna += 'T'
    elif i == 'T':
        new_dna += 'A'
    elif i == 'C':
        new_dna += 'G'
    elif i == 'G':
        new_dna += 'C'
print(new_dna)
