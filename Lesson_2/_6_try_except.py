"""
    try-except используется для перехвата исключений,
    чтоб программа не прекращала работу при возникновении ошибки.
"""

a = input("a = ")
b = input("b = ")
try:
    a = int(a)
    b = int(b)
    Result = a / b
except ValueError:
    print(a, "or", b, "not an iteger")
except NameError:
    print("not defined")
except ZeroDivisionError:
    print("division by zero")
except Exception as e:
    print(e.__class__.__name, ":", e)
else:
     print("result")
finally:
    print("finally")

print("out of try-except")