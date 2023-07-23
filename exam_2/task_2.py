# Найти в списке те элементы, значение которых меньше среднего арифметического,
# взятого от всех элементов списка.
import random
a = [random.randint(10, 90) for i in range(10)]
print(a)
sum = 0
for i in a:
    sum += i
print(sum)
var_sum = sum / 10
print(var_sum)
elem = []
for i in a:
    if i < var_sum:
        elem.append(i)
print(elem)