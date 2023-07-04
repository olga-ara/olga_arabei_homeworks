# Дан список чисел, если число встечается более 2х раз, то добавить его в новый список
from random import random
number = []
new_number = []
for i in range(9):
    x = int(random() * 10)
    number.append(x)
print(number)
for i in number:
    if number.count(i) > 2:
        new_number.append(i)
print(new_number)

