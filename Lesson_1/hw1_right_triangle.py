"""
    Площадь и периметр прямоугольного треугольника.
    1. С помощью input() вводятся катеты.
    2. Найти площадь треугольника.
    3. Найти периметр треугольника.
    4. Вывести результаты на экран.
"""

a = int(input("Введите первый катет треугольника: "))
b = int(input("Введите второй катет треугольника: "))
square = a * b / 2
c1 = a**2 + b**2
c = c1**0.5
perimeter = a + b + c
print("Первый катет = ", a)
print("Второй катет = ", b)
print("Площадь треугольника = ", square)
print("Периметр треугольника = ", perimeter)