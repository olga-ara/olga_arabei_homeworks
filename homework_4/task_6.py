# пользователь покупает автомобиль стоимостью 100_000 рублей, Если денег на счет достаточно, нужно списать деньги и
# вывести сообщение: поздравляю! вы купили автомобиль! а иначе вывести: у вас недостаточно средств, Не забудьте пожелать
# хорошего дня в любом случае

auto = 100_000
bank_account = int(input('сумма на счету клиента: '))
if bank_account >= auto:
    print(f'Поздравляю, вы купили автомобиль!!! Желаю Вам хорошего дня! Остаток средств на счету:{bank_account - auto}')
else:
    print(f'У Вас недостаточно средств для покупки автомобиля'
          f'  Хорошего Вам дня! ')