"""
    Строка имеет множетво методов.
    * Метод - это функция, которая привязана к конкретному объекту
    ** Строчные методы не изменяют строку, а возвращают новую
    Вызывается метод через . (точку) после объекта.
    Например вызов метода upper() у строки 'python':
    'python'.upper()  # PYTHON
    Чтобы посмотреть методы нужного объекта используйте функцию dir()
    print(dir(str)) - выведет все методы строк.
    Чтоб посмотреть описание метода (что делает и как использовать)
    используйте функцию help()
    print(help(str.upper)) - выведет описание метода upper
    Описание всех методов с примерами на русском языке
    https://pyprog.pro/python/py/str/str_methods.html
"""

s = "Hello World!"

# Метод для замены подстроки в строке - replace
# _____________________________________________

print(s.replace("World", "python"))  # Hello python!


# Методы для работа с регистром: upper, lower, title, capitalize, swapcase
# ____________________________________________________________
# upper - возводит всю строку к верхнему регистру
# lower - к нижнему
# swapcase - меняет все регистры на противоположные
# title - первую букву каждого слова к верхнему регистру
# capitalize - первую букву к верхнему, а остальные - к нижнему
# casefold - возвращает строку, подходящею для сравнения без регистра
print(s)  # Hello World!
print(s.upper())  # HELLO WORLD!
print(s.lower())  # hello world!
print(s.swapcase())  # hELLO wORLD!
print(s.title())  # Hello World!
print(s.capitalize())  # Hello world!
print(s.casefold())  # hello world!


# Методы для поиска первого вхождения подстроки в строку
# ______________________________________________________
# find - вернет индекс первого вхождения элемента, если не найдено - вернет -1
# index - аналогичен find, только если не найдено вызывает ValueError
# для поиска с конца строки используются rfind и rindex
# count - количество вхождений подстроки в строку

print(s.find("llo"))  # 2
print(s.find("P"))  # -1
print(s.rfind("l"))  # 9
print(s.index("l"))  # 2
print(s.rindex("l"))  # 2
# print(s.index('P'))  # ValueError
print(s.count("o"))  # 2


# Методы для удаление пробельных символов
# (только по краям строки, не в самом предложении)
# ________________________________________________
# strip - удаляет пробелы, переносы строк и табуляции слева и справа строки
# lstrip - только слева, rstrip - только справа

string = "   Hello world  \t  "
print(string.strip())  # Hello world
print(string.rstrip())  #    Hello world
print(string.lstrip())  # Hello world  \t


# Методы для проверки символов.
# _____________________________
# isdigit - проверяет, состоит ли строка только из цифр
# isalpha - только из букв
# isnumeric - только из чисел
# isalnum - только и букв и цифр
# isspace - только пробельные символы
print("123".isdigit())  # True
print("½".isdigit())  # False
print("½".isnumeric())  # True
print("abc123".isalpha())  # False
print("abc123".isalnum())  # True
print(" \n \t".isspace())  # True


# Методы для проверки регистра элементов строки
# _____________________________________________
# isupper, islower, istitle, iscapitalize
print("ABC".islower())  # False
print("ABC".isupper())  # True


# Методы для проверки начала и конца строки
# _________________________________________
# startswith - начинается ли строка с подстроки
# endswith - заканчивается ли строка подстрокой
print(s.startswith("Hello"))  # True
print(s.endswith("!!!"))  # False


# Методы для разбиения и склеивания строк
# _______________________________________
# split - разбивает строку на элементы по указанному разделителю
# splitlines - разбивает текст на список строк
# join - склеивает элементы с указанным разделителем

string = "bmw-mercedes-audi"

print(string.split("-"))  # ['bmw', 'mercedes', 'audi']
print(", ".join(string.split("-")))  # bmw, mercedes, audi


# Методы для центрирования содержимого строки
# ___________________________________________

# делает длину строки не меньше 20, заполняя первые символы пробелами
print(s.rjust(20))
# делает длину строки не меньше 20, заполняя последние символы '!'
print(s.ljust(20, "!"))
# центрирует строку, добавляет '!' в начало и конец строки
print(s.center(20, "!"))