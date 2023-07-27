# 1)	Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры:
# операции + - * / и два числа. Операции являются функциями. Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return None


while True:

    operation = input("Выберите действие: +,-,*,/ или 0 - для выхода из программы ")

    if operation == '0':
        break

    num1 = float(input("Введите число: "))
    num2 = float(input("Введите число: "))

    if operation == '+':
        print(num1, "+", num2, "=", add(num1, num2))

    elif operation == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif operation == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif operation == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Неверная операция")