"""
    Вводится год.
    Программа выводит количество дней в году, учитывая високосный год.
    * високосный год кратный 4, но не кратный 100 или кратный 400
"""

a = int(input("Укажите год: "))
if a % 4 != 0:
    print("365")
elif a % 100 == 0:
    if a % 400 == 0:
        print("366")
    else:
        print("365")
else:
    print("366")