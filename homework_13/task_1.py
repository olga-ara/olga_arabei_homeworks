# задача
# Напишите программу, которая запрашивает у пользователя данные о студентах и сохраняет их в файл формата CSV.
# Требования:
# Программа должна запрашивать у пользователя информацию о каждом студенте, включая имя, фамилию и возраст.
# Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV.
# Файл CSV должен иметь следующие заголовки столбцов: "Имя", "Фамилия", "Возраст".
# Программа должна продолжать запрашивать информацию о студентах до тех пор, пока пользователь не введет команду "stop" для завершения.
# В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.
csv = ''
import csv
with open('students.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    while True:
         name = input('Введите имя студента: ')
         if name == 'stop':
              print('Данные успешно сохранены.')
              break
         surmame = input('Ввведите фамилию студента: ')
         age = input('Введите возраст студента: ')
         data_base = [name, surmame, age]
         writer.writerow(data_base)
