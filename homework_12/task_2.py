# 2 Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

file_txt = open("task_2.txt", 'w')
string = True
while string:
    string = input('Введите данные посторочно: ')
if string:
    file_txt.write(string + '\n')
    print(string)
else:
    print('Конец программы')
file_txt.close()

