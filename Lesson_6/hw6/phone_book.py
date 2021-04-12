"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
    ...
"""
import string


with open("phone_book.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    for char in string.punctuation:
        if char in data:
            data = data.replace(char, "")
            f.seek(0)
    f.seek(0)
    name = ""
    for char in data:
        if char.isalpha:
            name += char
        f.seek(0) 
    phone = ""
    for char in phone:
        if char.isdigit:
            phone += char
        f.seek(0)     
    TEMPLATE = "+380{phone} - {name}"
print(TEMPLATE.format()
                
with open("edited_phone_book.txt", "a+") as editedf:
    print(TEMPLATE.format(), file=editedf)
