# Даны несколько списков:
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).
list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, 4, 0, 23, 6, 34]
list1.sort(reverse=True)
print(list1[-2])
list2.sort(reverse=True)
print(list2[-2])
list3.sort(reverse=True)
print(list3[-2])
