# Есть список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу:
# например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
# само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).

list_1 = [1, 25, 25, 16, 25, 16, 16, 16, 99, 25, 99]
new_set = set()
for i in list_1:
    number = list_1.count(i)
    new_set.add(str(i)*number)
print(new_set)

