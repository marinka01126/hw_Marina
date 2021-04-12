string = "Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry."

# 1. Удалить из строки символы ','.
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
string = string.replace(",", "")
print("1.", string)

# 2. Найти индекс самой последней буквы 'i' в строке.
#    Результат: 49

print("2.", string.rfind("i"))

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

print("3.", string.lower().count("i",))

# 4. Найти и вывести срез строки от 3 буквы 's' до 6 пробела.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов, вторым
#     параметром можно передать индекс, от которого делать поиск find('s', 12))
"""не поняла как решить..."""

print("4.", string[3:6]) 

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
print(len(string))
print(string[:29]*3+string[29:])