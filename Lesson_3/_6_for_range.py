"""
    Для генерации числовых последовательностей используется функция range()
    range(start[, end[, step])
    В математике - последовательность [start; end) - т.е. end не включается
"""

range(10)
range(1, 7)
range(1, 10, 2)

range(10, 1, -2)
for i in range(10), 1, -2:
    print(i)

for i in range(2, 21, 2):
    print(i)

for _ in range(1, 10):
    print("hello")