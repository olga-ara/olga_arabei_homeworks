# 5 Есть словарь песен группы Depeche Mode
violator_songsdict = {'World in My Eyes': 4.76,
                      'Sweetest Perfection': 5.43,
                      'Personal Jesus': 4.56,
                      'Halo': 4.30,
                      'Waiting for the Night': 6.07,
                      'Enjoy the Silence': 4.6,
                      'Policy of Truth': 4.88,
                      'Blue Dress': 4.18,
                      'Clean': 5.68, }
# Выведите общее время звучания всех песен.
print(violator_songsdict.values())
sum_values = 0
for key, value in violator_songsdict.items():
    sum_values += value
print(sum_values)

# Создайте список песен, время звучаниях которых больше 5 минут
list_song_5 = []
for key, value in violator_songsdict.items():
    if value > 5:
        list_song_5.append(key)
print(list_song_5)

# Создайте новый словарь тех песен, название которых состоит из 1 слова
dict_song_1 = {key: violator_songsdict[key] for key in violator_songsdict.keys() if not ' ' in key}
print(dict_song_1)

