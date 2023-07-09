# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет. (Пример введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.

import random
var_numbers = random.randint(1, 10)
red_black = random.randint(1, 2)
win_color = []

if red_black == 1:
    win_color.append('красный')
elif red_black == 2:
    win_color.append('черный')
new_comb = " ".join(win_color)
win_result = str(var_numbers) + ' ' + new_comb
print(f'Верная комбинация: {win_result}')

tryies = 6  # количество попыток

while True:
    win_combo = input('сделайте ставку (число и цвет): ')
    tryies -= 1
    if tryies == 0:
        print('К сожалению, у Вас закончились попытки.')
        break
    if win_combo == win_result:
        print(f'ваша ставка {win_combo} сыграла! Вы выиграли 1_000_000')
        break
    else:
        print(f'Вы проиграли...Выиграшная комбинация {win_result}')
