# Дан список чисел c дубликатами, создать новый список, в котором будут только уникальные числа
from random import random
numbers = []
unique_numbers = list(set(numbers))
for i in range(12):
    x = int(random() * 10)
    numbers.append(x)
print(numbers)
for i in numbers:
    if numbers.count(i) == 1:
        unique_numbers.append(i)
print(unique_numbers)

# второй способ еще подумаю)
