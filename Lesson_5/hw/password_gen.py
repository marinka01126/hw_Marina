"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

from random import choice, randint, sample
from string import digits, punctuation, ascii_lowercase, ascii_letters, ascii_uppercase

def main():
    while True:
        print(
            "1. Сгенерировать простой пароль",
            "2. Сгенерировать средний пароль",
            "3. Сгенерировать сложный пароль",
            sep="\n",
        )
        menu_item = input("Выберите пункт меню: ")
        if menu_item == "1":
            psw = ""
            while len(psw) < 8:
                char = choice(ascii_lowercase)
                psw = psw + char
            print(psw)
            if input("Continue? (y/N) ") != "y":
                break
        if menu_item == "2":
            psw = ""
            while len(psw) < 8:
                tmp = ascii_letters + digits
                char = choice(tmp)
                psw = psw + char
            print(psw)    
            if input("Continue? (y/N) ") != "y":
                break
        if menu_item == "3":
          #  psw = ""
          #  tmp = ascii_letters + ascii_lowercase + ascii_uppercase + digits + punctuation
          #  psw_length = randint(8, 16)
          #  for tmp in range(psw_length): #and psw.count(ascii_uppercase) == 1 and psw.count(ascii_lowercase) == 1 and psw.count(digits) == 1 and psw.count(punctuation) == 1
          #      char = choice(tmp)
          #  psw = psw + char
          #  print(psw)
            characters = ascii_letters + punctuation  + digits

            password = ""
            password_length = randint(8, 16)

            for x in range(password_length):
                char = choice(characters)
                password = password + char

            print(password)
            if input("Continue? (y/N) ") != "y":
                break

if __name__ == "__main__":
    main()