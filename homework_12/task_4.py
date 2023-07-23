# 4) Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом,
# то должна выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.

difference_1 = input('Введите первое значение:  ')
difference_2 = input('Введите второе значение:  ')

try:
    difference_1 = float(difference_1)
    difference_2 = float(difference_2)
    print(difference_1 + difference_2)
except ValueError:
    print(str(difference_1) + str(difference_2))
else:
    print(f'Все верно, вы ввели 2 числа {difference_1} и {difference_2}')
finally:
    print('Программа завершена')
