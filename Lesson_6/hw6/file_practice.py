"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open("file_practice.txt", "w") as f:
    print("Starting practice with files", file=f)


"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

with open("file_practice.txt", "r") as f:
    data = f.read(5)
    print(data)
    data = f.seek(0)
    data = f.read()
    print(data)



"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

with open("text.txt", "r+") as text:
    data_2 = text.read()
    print(data_2)
    text.seek(0)
    print("Количество букв i: ", data_2.count("i")+data_2.count("I"))
    print("Количество букв e: ", data_2.count("e")+data_2.count("E"))
    if data_2.count("i")+data_2.count("I") > data_2.count("e")+data_2.count("E"):
        data_2 = data_2.replace("i", "e")
        data_2 = data_2.replace("I", "E")
    else:
        data_2 = data_2.replace("e", "i")
        data_2 = data_2.replace("E", "I")
with open("file_practice.txt", "a") as f:
    print(data_2, file=f)


"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

with open("file_practice.txt", "r+") as f:
    data = f.read()
    
    print("Число символов в file_practice.txt :", len(data))
    if len(data) % 2 == 0:
        print("четное количество элементов")
        print("\nthe end", file=f)
    else:
        print("нечетное количество элементов")
        print("\nbye", file=f)


"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""
with open("file_practice.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    n = len(data)//2
    a = input("Напишите строку для вставки в текст: ")
    n2 = len(a)
    new_data = data[:n] + a + data[n+n2:]
    print(new_data, file=f)