# 3)В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов.
# входные данные:
""" Hello world 1235
Hello world 2
hello world 345
"""
with open("task_3.txt", 'r') as f:
    task_3 = f.readlines()
for i in task_3:
    print("Количество строк", len(i.split()))
    print("Количество символов", len(i.replace("\n", '')))


