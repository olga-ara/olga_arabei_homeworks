# 1)Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.
import re

with open('task_1.txt', 'r') as file:
    list_1 = file.readlines()
    print(list_1)
    clean_read = [i.rstrip() for i in list_1]
    print(clean_read)
numbers = []
strings = []
for i in clean_read:
    if i.isdigit():
        numbers.append(i)
    else:
        strings.append(i)
numbers.sort()
strings.sort()
print(numbers + strings)
