# определить существование треугольника, а также его тип
print("Введите значение трех точек не лежащих на одной прямой: a, b, c:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("треугольник существует")
else:
    print("треугольник не существует")

# определить тип треугольника
if c ** 2 < a ** 2 + b ** 2:
    print("треугольник - остроугольный")
if c ** 2 == a ** 2 + b ** 2:
    print("треугольник - прямоугольный")
if c ** 2 > a ** 2 + b ** 2:
    print(" треугольник тупоугольный")
