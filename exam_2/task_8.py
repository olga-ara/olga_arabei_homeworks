# Напишите программу, которая подключает модуль math и,
# используя значение числа \pi  из этого модуля,
# вводим радиус круга и находим периметр этого круга, результат вывести на экран.
import math
radius = float(input("введите значение радиуса круга: "))
perimetr_circle = 2 * math.pi * radius
print(perimetr_circle)
