a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

print(f"Числа Армстронга от {a} до {b}")

if b > a:
    for num in range(a, b + 1):
        sum_digits_cube = 0
        for item in str(num):
            sum_digits_cube += int(item) ** 3
        if num == sum_digits_cube:
            print(num)

if a > b:
    for num in range(b, a + 1):
        sum_digits_cube = 0
        for item in str(num):
            sum_digits_cube += int(item) ** 3
        if num == sum_digits_cube:
            print(num)