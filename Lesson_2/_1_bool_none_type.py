"""
    Логический тип данных bool
    Может иметь значение True либо False
"""
active = True
deleted = False

print(active, type(active))
print(deleted, type(deleted))

"""
    bool находится в подмножестве int, поэтому преобразовывается в числа
    и для него доступны все арифметические операции, как и для чисел
"""
print(int(active))
print(int(deleted))
print(True + True)
print(2 + True * False ** 0)

"""
    Приведение к типу bool
"""

# 1. Числа
# все числа, кроме 0 - True, сам 0 - False
a = 0
b = -123
print(bool(a))
print(bool(b))

# 2. Последовательности (строки, списки, кортежи, множества, словари)
# пустая последовательность - False, заполненная - True
print(bool(''))
print(bool(" "))
print(bool([0, 0, 0]))

"""
    Тип данных NoneType
    Для хранения пустых значений используется None
"""

status = None
print(status, type(status))