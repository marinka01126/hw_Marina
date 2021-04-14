"""
    Нарисовать границу из * в списке.
    Количество элементов каждой строки уравнять по самой длинной в списке,
    центрировать текст и недостающие символы заполнить пробелами.

    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['py',
             'python']

    [out]   ['********',
             '*  py  *',
             '*python*',
             '********']

    Покрыть несколькими тестами.
"""
from pprint import pprint

list_ = ['py', 'django']

count = int()
for i in max(list_, key=len):
    count += 1
print(count)
print("* " * (count +1))
for _ in range(count - 2):
    print("* ", list_[0], list_[1], "* ")
print("* " * (count + 1))

