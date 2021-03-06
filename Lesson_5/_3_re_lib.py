"""
    Библиотека re содержит функции для работы со строками
    с использованием регулярных выражений.
    Документация (python-3.9.1) https://docs.python.org/3/library/re.html
    Основные регулярные выражения:
    r'\d' - любая цифра
    r'\D' - любая не цифра
    r'\w' - любая буква либо цифра
    r'\W' - любая не буква и не цифра
    r'\s' - пробельный символ
    r'\S' - любой символ, кроме пробельных
    Так же можно определять последовательности символов (язык важен!):
    r'[a-z]' - любая строчная буква от a до z
    r'[А-Я]' - любая заглавная буква от А до Я
    r'[a-zA-Z]' - любая буква от a до Z (строчные и заглавные)
    r'[0-9]' - любая цифра от 0 до 9
    r'[a-z0-9A-Z]' - любая буква (латиница) либо цифра от 0 до 9
    Определение количества символов:
    r'\d{2}' - последовательность 2х любых цифр
    r'[a-z]{5}' - последовательность 5 любых строчных букв
    r'[a-zA-Z]+' - последовательность латинских букв длиной 1 и больше (слова)
"""  # noqa: W605

import re

string = "Hello, world!123"


# -----------------------------------------------------------------------------
# Метод re.sub(pattern, repl, string)
# Работает как строчный replace(), только можно использовать регулярки

# заменяет все цифры (\d) на восклицательный знак (!) в строке string
print(re.sub(r"\d", "!", string))  # Hello, world!!!!

# заменяет все не цифры (\D) пустой строкой (оставляет только цифры)
print(re.sub(r"\D", "", string))  # 123

# заменяет все последовательности букв (слова) на прочерк (-)
print(re.sub(r"[a-zA-Z]+", "-", string))  # -, -!123

# можно использовать как replace и без регулярных выражений
print(re.sub("world", "friend", string))  # Hello, friend!123
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Метод re.findall(pattern, string)
# Возвращает список всех найденных совпадений по шаблону

# выводит список всех последовательностей латинский букв (слов)
print(re.findall(r"[a-zA-Z]+", string))

# выводит список всех не букв и не цифр (\W)
print(re.findall(r"\W", string))

number = "+38 (073) 123-45-67"
# находим список всех цифр (\d) в строке number
all_digits = re.findall(r"\d", number)
print("".join(all_digits))
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Метод re.split(pattern, string, [maxsplit=0])
# Работает как строчный split(), только можно использовать регулярки

# разделим строку string по не букве и не цифре (\W)
print(re.split(r"\W", string))
test_string = "python0is1the2best3lang"
# разделим строку test_string по любой цифре
print(re.split(r"\d", test_string))
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Метод re.search(pattern, string)
# Ищет первое вхождение заданого шаблона в строке

# Метод re.match(pattern, string) работает аналогично,
# только ищет вхождение в начале строки, а не во всей строке

result = re.search(r"\w+", string)
print(result.group())
print(result.start())
print(result.end())
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Регулярное выражение (паттерн) можно собрать в отдельный объект
# re.compile(pattern)

# Создаем объект с паттерном (последовательность из 1 и более букв)
pattern = re.compile(r"[a-zA-Z]+")
# У созданного объекта есть все основные методы библиотеки re
print(pattern.findall(string))
print(pattern.sub("---", string))
# -----------------------------------------------------------------------------