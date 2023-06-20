# Вычислить сумму цифр случайного трехзначного числа*
num = int(input('введите трехзначное число '))  # 359
# представим число так n - 'это сотни, u - это десятки, m - это единицы
m = num % 10  # получим остаток от деления
print(m)
num = num // 10  # откидываем остаток от деления на цело
print(num)
u = num % 10  # получаем десятки
print(u)
n = num // 10  # получаем цифру от сотен делением на цело
print(n)
print(n + u + m) #складываем цифры

# второй вариант решения
import random
num = random.randrange(100, 999)
print(num)
num = str(num)
num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])
result = (num1 + num2 + num3)
print(result)


