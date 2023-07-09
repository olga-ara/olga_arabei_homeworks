# Создайте словарь тремя способами. выведите полученный словарь на экран
dictionary_1 = {'1': 0, '2': 0, '3': 0}
print(dictionary_1)

key = [1, 2, 3]
value = [0, 0, 0]

dictionary_2 = dict([(1, 0), (2, 0), (3, 0)])
print(dictionary_2)

dictionary_3 = dict.fromkeys(['1', '2', '3'], 0)
print(dictionary_3)

dictionary_4 = dict(zip([1, 2, 3], [0, 0, 0]))
print(dictionary_4)


