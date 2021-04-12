"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл passwords.txt
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    3*. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""
from random import choice, randint, sample
from string import digits, punctuation, ascii_lowercase, ascii_letters, ascii_uppercase

with open("passwords.txt", "a+") as f:
    f.write("passwords:\n")

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
                print(psw, file=f)
                if input("Continue? (y/N) ") != "y":
                    break
            if menu_item == "2":
                psw = ""
                while len(psw) < 8:
                    tmp = ascii_letters + digits
                    char = choice(tmp)
                    psw = psw + char
                print(psw, file=f)    
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

                print(password, file=f)
                if input("Continue? (y/N) ") != "y":
                    break

    if __name__ == "__main__":
        main()