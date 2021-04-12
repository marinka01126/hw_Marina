# 1. Вывести на экран парные числа от 2 до 50
for i in range(2, 50):
    if i % 2 == 0:
        print(i)

for i in range(2, 50, 2):
    print(i)


# 2. Вывести числа кратные 3, но не кратные 5 от 1 до 50
for i in range(3, 50):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

for i in range(3, 50, 3):
    if i % 5 != 0:
        print(i)

# 3. Вывести числа от 1 до 25 в 3 степени
for i in range(1, 25):
    print(i**3)