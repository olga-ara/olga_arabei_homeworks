# Дан список. Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных. Вывести всё на экран.
list_s = [15, 48, 'hello', 6, 19, 'world']
num_of_list = []
litera_in_list = []
sum_of_num = 0
for i in list_s:
    if type(i) == int:
        num_of_list.append(i)
    else:
        litera_in_list.append(i)
print(num_of_list)
print(litera_in_list)
new_numbers = []
for i in num_of_list:
    if i % 2 == 0:
        if i >= 10:
            a = i // 10
            b = i % 10
            c = a + b
            new_numbers.append(c)
        else:
            new_numbers.append(i)
    else:
        new_numbers.insert(i, 1)
print(f'вывести новый список после операций {new_numbers}')

string_litera_in_list = ''.join(litera_in_list)
print(string_litera_in_list)
glas = 'aeiouy'
gls = []
sgl = []
for i in string_litera_in_list:
    if i in glas:
        gls.append(i)
    else:
        sgl.append(i)
print(f'список согласных {sgl} и список {gls}')
print(len(sgl))
print(len(gls))
