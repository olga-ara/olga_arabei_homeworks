# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

from random import random
num = 10
massive = []
low = int(input('Нижняя граница массива: '))
high = int(input('Верхняя граница массива: '))
for i in range(num):
    n = int(random()*(high-low)) + low
    massive.append(n)
print(massive)
print('Удаляемый диапазон')
low = int(input('   нижняя граница: '))
high = int(input('   верхняя граница: '))
i = 0
m = num
while i < m:
    if low <= massive[i] <= high:
        del massive[i]
        m -= 1
    else:
        i += 1
for i in range(m, num):
    massive.append(0)
print(massive)