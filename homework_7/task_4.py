# Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n включительно
# в порядке возрастания, если m<n, или в порядке убывания в противном случае.

m = int(input('Введите число m: '))
n = int(input('введите число n: '))

context = []
revers = []
if m < n:
    for i in range(m, n+1):
        context.append(i)
        context.sort()
    print(context)
else:
    for i in range(n, m+1):
        revers.append(i)
        revers.sort(reverse=True)
    print(revers)
