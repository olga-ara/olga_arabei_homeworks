# Найти результат выражения, переменная вводиться с клавиатуры
# нужно разбить выражение на составляющие
a = int(input('введите число '))
# для каждой части вводим переменную, результат обозначим как 'y'
drop1 = 1 + a + a ** 2 / 2 * a + a ** 2
drop2 = 1 - a + a ** 2 / 2 * a - a ** 2
drop3 = 5 - 2 * a ** 2
y = (drop1 + 2 - drop2) * (-1) * drop3
print(drop1)
print(drop2)
print(drop3)
print(y)
