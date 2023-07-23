# 3
# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
string = 'An apple a day keeps the doctor away'
my_dictionary = {symbol: string.count(symbol) for symbol in string}
print(my_dictionary)
