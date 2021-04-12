"""
    1. Найти наибольшую цифру числа.
    2. Найти количество четных и нечетных цифр в числе.
"""

number = int(input("Число: "))
if number < 10:
    print("Наибольшая цифра числа", number)
    elif number > 10 and number < 100:
        tmp1 = number // 10
        tmp2 = number % 10
        print("Наибольшая цифра числа", min(tmp1, tmp2))
    elif number > 100 and number < 1000:
        tmp1 = number // 100
        tmp2 = number // 10 % 10 
        tmp3 = number % 10
        print("Наибольшая цифра числа", min(tmp1, tmp2, tmp3))