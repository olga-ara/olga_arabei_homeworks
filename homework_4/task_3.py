# Пользователь вводит 3 числа, если все числа больше 10, вывести yes, иначе - no
print("Введите три числа: ")
number1 = float(input("число 1 = "))
number2 = float(input("число 2 = "))
number3 = float(input("чиcло 3 = "))
if number1 > 10 and number2 > 10 and number3 > 10:
    print("yes")
else:
    print("no")

