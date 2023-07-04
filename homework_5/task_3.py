# вывести на экран все четные значения в диапазоне от 1 до 497
even = ""
for i in range(1, 498):
    if i % 2 == 0:
        even += str(i) + " "
print(even)