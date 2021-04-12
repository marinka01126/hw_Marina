"""
    Модифицируйте форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""

with open("users.txt", "a+", encoding="utf-8") as usersfile:
    usersdata = usersfile.read()

    def main():
        answer1 = get_phone()
        answer2 = get_email()
        answer3 = get_psw()
        print("\nПоздравляем с успешной регистрацией!", file=usersfile)
        print(f'Ваш номер телефона: {answer1}', file=usersfile)
        print(f'Ваш email: {answer2}', file=usersfile)
        print(f'Ваш пароль: {answer3}', file=usersfile)


    def get_phone():
        answer1 = input('Введите ваш номер телефона ')
        if is_valid_phone(answer1):
            print("OK")
        else:
            print("Invalid phone number")
            return get_phone()
        return answer1

    def is_valid_phone(answer1):
        if len(answer1) != 12:
            return False
        if not answer1.startswith("380"):
            return False
            # if len(s) != 12 or not s.swartswith("380"):
        return answer1

    def get_email():
        answer2 = input('Введите ваш email ')
        if len(answer2) > 6 and answer2.count("@"):
            print("OK")
        else:
            print("Invalid email")
        return answer2

    def get_psw():
        answer3 = input('Введите ваш пароль ')
        if len(answer3) > 8: 
            print("OK")
        else:
            print("пароль должен быть больше 8 символов")
        return answer3
    if __name__ == "__main__":
        main()

    