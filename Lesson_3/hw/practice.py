"""
    Реализовать программу, с помощью которой можно (меню):
    1. Найти наибольшую цифру числа n.
    2. Найти количество четных и нечетных цифр в числе n.
    3. Узнать, является ли число n простым.
    4. Отобразить ряд простых чисел от 2 до n через запятую.
"""

while True:
    print(
        "1. Найти наибольшую цифру числа n.",
        "2. Найти количество четных и нечетных цифр в числе n.",
        "3. Узнать, является ли число n простым.",
        "4. Отобразить ряд простых чисел от 2 до n через запятую.",
        sep="\n",
    )
    menu_item = input("Выберите пункт меню: ")
    if menu_item == "1":
        n = int(input("Введите число от 1 до 999 "))
        if n > 0 and n < 10:
            print("Наибольшая цифра вашего числа ", n)
        elif n >= 10 and n <= 99:
            n1 = n // 10
            n2 = n % 10
            print("Наибольшая цифра вашего числа ", max(n1, n2))
        elif n >= 10 and n <= 999:
            n1 = n // 100
            n2 = n % 100 // 10
            n3 = n % 10
            print("Наибольшая цифра вашего числа ", max(n1, n2, n3))
        else:
            print("Введено недопустимое значение")
        if input("Continue? (y/N) ") != "y":
            break
    if menu_item == "2":
        a = input("Введите ваше число ")
        digits = "02468"
        
        even = 0
        odd = 0
        
        for i in a:
            if i in digits:
                even += 1
            else:
                odd += 1
        
        print("Четных : ", even, ",", "Нечетных: ", odd)
        if input("Continue? (y/N) ") != "y":
            break
    if menu_item == "3":
        n = int(input("Введите Ваше число "))
        import math

        if n < 2:
            print("Число должно быть больше 2")
            quit()
        elif n == 2:
            print("Это простое число")
            quit()

        i = 2
        limit = int(math.sqrt(n))

        while i <= limit:
            if n % i == 0:
                print("Это составное число")
                quit()
            i += 1

            print("Это простое число")
        if input("Continue? (y/N) ") != "y":
            break
    if menu_item == "4":
        n = int(input("Введите ваше число "))
        for i in range(2, n, 2):
            print(i+1, ",")
