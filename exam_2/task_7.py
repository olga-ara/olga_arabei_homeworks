# Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
# Также, если эта центральная буква равна первой букве в строке,
# то создать и вывести часть строки между первым и последним символами исходной строки.
# (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
# Для создания результирующий строки используйте срез)
my_string = input('введите строку: ')
size_str = (len(my_string))
print(size_str)
middle_str = size_str // 2
if size_str % 2 == 0:
    print(middle_str - 1)
else:
    print(middle_str)
print(my_string[middle_str])
if my_string[middle_str] == my_string[0]:
    print(my_string[1:-1])
