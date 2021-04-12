"""
    Особенности описания чисел в коде.
"""

# Объявить читаемое длинное число можно использовав _ как разделитель

big_number = 42_123_333_123
print(big_number)

# float числа являются не точными и при операции иногда встречаются погрешности
print(0.1 + 0.2)

# для описания очень маленьких или очень больших чисел можно использовать e
print(155e-05)
print(12e5)

"""
    Встроенные функции python для работы с числами
"""

# abs() - получить значение числа по модулю
print(abs(-123))

# round(num, ndigits) - округлить число num до ndigits знаков после запятой
# !!! Стоит обратить внимание, что round округляет "банковским" методом
print(round(3.1415, 2))

# pow(base, exp, mod) - возведение числа base в степень exp, аналог base ** exp
# передав необязательного аргумента mod - результат разделится по модулю на mod
print(pow(3, 10))

# min()/max() - возвращает минимальное/максимальное значение
print(min(14.23, -3.14, 123, -17))
print(max(14.23, -3.14, 123, -17))

# sum() - возвращает сумму переданной последовательности
a = 10
b = 20
c = 30

# необходимо передавать либо кортеж () либо список []
print(sum((a, b, c)))

# divmod(x, y) - возвращает частное и остаток от деления x на y в виде кортежа
print(divmod(17, 5))