"""
    Операторы сравнения: >, <, >=, <=, ==, !=
    В результате сравнении объектов получаем True либо False
"""

a = 10
b = 20

print(a < b)
print(a == b)

"""
    Логические операторы: and (и), or (или), not (не)
"""

# Выражение с успользованием оператора and истинно только тогда,
# когда истинны все операнды.

print(1 < 2 and 2 < 3)
print(1 < 2 and  2 < 3 and 3 > 4)

# Выражение с успользованием оператора or истинно тогда,
# когда хоть один операнд - истина.

a = 10
print(a < 0 or a == 10)
print(a == 0 or a + 2 < 3 or a > 1)

# Оператор not (не) меняет булевое значение на противоположное

print(not False)
print(not True)

b = -10 * 2
c = "python"
print(not b == 20 and b < 1)
# not b == 20 (екв. b != 20) - True и b < 1 - True


"""
    Операторы is, is not
    Применяются с bool и NoneType
"""

active = True
deleted = False
status = None

print(active is False)
print(deleted is not None)
print(status is None)

result = None
a = 20
b = 20
if a < b:
    result = 10
elif a == b:
    result = 0

if result is not None: 
    print(result)