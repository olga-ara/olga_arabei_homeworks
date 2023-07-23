# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
# data = ['Вечерело\n',
#         'Жужжали мухи\n',
#         'Светил фонарик\n',
#         'Кипела вода в чайнике\n',
#         'Венера зажглась на небе\n',
#         'Деревья шумели\n',
#         'Тучи разошлись\n',
#         'Листва зеленела\n']

import os.path
# def longest_words(file):
#     with open('article.txt', 'w', encoding='cp1251') as file:
#         words = file.read().split()
#         max_length = len(max(words, key=len))
#         sought_words = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words
#
#
# print(longest_words('article.txt'))
#
import os.path
#
# def longest_words(file):
#     with open(r"C:\Users\Vladislav Stazharov\PycharmProjects\pr4\test.txt", "r") as text:
#         words = text.read().split()
#         max_length = len(max(words, key=len))
#         sought_words = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words
#
#
# print(longest_words('article.txt'))









with open('article.txt', 'w', encoding='cp1251') as file:
    list1 = []
    while True:
        a = file.readline().strip()
        if not a:
            break
        list1 += a.split()
    def longest_words(prem):
        b = 'a'
        c = 'a'
        for i in prem:
            if len(i) == len(b):
                c = c + ' '
                c = c + i
                b = i
            elif len(i) > len(b):
                c = b = i
        return c
print(longest_words(list1))
