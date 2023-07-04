# Есть список с четными и нечетными элементами, посчитать количество четных и нечетных элементов
from random import random
number = []
for i in range(15):
    x = int(random() * 100)
    number.append(x)
print(number)

even = 0  # количество четных чисел
odd = 0  # количество нечетных чисел
for i in number:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'четных {even}')
print(f'нечетных {odd}')