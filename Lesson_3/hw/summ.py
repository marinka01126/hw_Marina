"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.
    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.
    * обработать возможные ошибки
"""

start = int(input("Начало числового ряда "))
end = int(input("Конец числового ряда "))

suma = 0
mult = 1
 
for digit in range(start, end):
    suma += int(digit)
    mult *= int(digit+1)
 
print("Сумма:", suma)
print("Произведение нечетных:", mult)
