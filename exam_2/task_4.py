# Ввести 10 чисел с клавиатуры, данные числа добавить во множество.

ten_numbers = set()
counter = 10
while counter != 0:
    number = int(input('введите число: '))
    counter -= 1
    ten_numbers.add(number)
print(ten_numbers)
