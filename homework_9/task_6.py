# дан словарь ,,,Добавить каждому ключу число равное длине этого ключа

dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dict = {}
for key in dict.keys():
    new_key = key + str(len(key))
    new_dict[new_key] = dict[key]
print(new_dict)