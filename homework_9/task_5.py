# выведите статистику частности букв в кортеже
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(long_word)
count_litera = {}
for i in long_word:
    if i in count_litera.keys():
        continue
    else:
        count_litera[i] = long_word.count(i)
print(count_litera)

