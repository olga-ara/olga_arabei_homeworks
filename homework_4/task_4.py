# Пользователь вводит 2 числа, если числа отличаются  друг от друга на 135 вывести yes, иначе - no
print("Введите 2 числа: ")
number1 = float(input("число 1 = "))
number2 = float(input("число 2 = "))

if number1 - number2 == 135 or number2 - number1 == 135:
    print("yes")
else:
    print("no")
