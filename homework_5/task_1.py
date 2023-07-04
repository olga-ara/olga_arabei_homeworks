# Перемножить все нечетные числа в диапазоне от 1 до 100

multi = 1
for i in range(1, 100, 2):
    if i % 2 != 0:
        multi = multi*i
print(multi)