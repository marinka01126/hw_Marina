"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.
    В зависимости от введенного оператора,
    между числами проводится определенная операция.
    Результат выводится на экран.
    * обработать все возможные ошибки программы с помощью try-except
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = input("Введите действие: ")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
try:
    result = a / b
except ValueError:
    print(a, "or", b, "not an iteger")
except NameError:
    print("not defined")
except ZeroDivisionError:
    print("division by zero")
except Exception as e:
    print(e.__class__.__name, ":", e)
else:
    print(result)   