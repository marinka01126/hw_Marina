"""
    1. Вводим строку.
    Если длина строки больше 5, вывести первые три символа в верхнем регистре и
    последние три символа в нижнем регистре.
    Иначе вывести первый символ с измененным регистром столько раз,
    какова длина строки.
"""

# s = input('1. Enter some string: ')
s = "Hello ! ; , woRlD"

# Проходим циклов по тем знакам, которые нужно убрать и делаем replace()
for i in "!-;,.":
    s = s.replace(i, "")
    print(s)