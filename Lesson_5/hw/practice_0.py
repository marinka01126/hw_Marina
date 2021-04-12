"""
    Напишите функцию, которая не принимает водных параметров,
    запрашивает у пользователя username, валидирует его и возвращает.
    Валидации:
    - мимимальное количество символов 6 (len)
    - максимальное количество симолов 20 (len)
    - доступны только латинские буквы в нижнем регистре и _ (in, string lib)
    - username не может начинаться символом _ (.startswith())
    Если какое-то из требований не выполняется, запрашиваем повторный ввод.
    * смотрите lesson5/_6_practice_valid.py
"""

from string import ascii_lowercase

def main():
    username = input("Введите username: ")
    if get_username(username):
        print(f"Добро пожаловать, {username}!")
    else:
        print("Повторите ввод")
    
    
def get_username(username):
    while username in ascii_lowercase:
        if len(username) < 6 or len(username) > 20:
            print("Допустимая длина username от 6 до 20 символов")
        elif username.startswith("_"):
            print("username не может начинаться символом _")
        else:
            print("доступны только латинские буквы в нижнем регистре и _")
        

if __name__ == "__main__":
    main()