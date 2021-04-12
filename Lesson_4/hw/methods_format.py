"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "здесь_исходная_строка".
        Результат: "здесь_измененная_строка_после_выполненного_пункта".
    (Использовать форматирование строк f'{}')
"""

# можно заменить данную строку на input()
string = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."
counter_l = counter_u = 0

for char in string:
    if char.islower():
        counter_l += 1
    elif char.isupper:
        counter_u += 1
    break
if counter_l > counter_u:
    print("Исходная строка: ", string)
    print("Результат 1:", string.lower())     
else:
    print("Исходная строка: ", string)
    print("Результат 1: ", string.swapcase())
        

string2 = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."
if string2.isupper():
    string2 = "Done. " + string2
else:
    string2 = string2.replace(string2[:5], "draft: ") + string2[6:]
print("Результат 2: ", string2)

string3 = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."
if len(string3) >= 20:
    print("Результат 3: ", string3[:20])
else:
    print("Результат 3", string3.ljust(20, "@"))