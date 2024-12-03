number = input("Введите пункт задачи:")


# --------------------------------------------------------

if number == "A" or number == "a":
    x_a = int(input("Введите число:"))

    sum_digits = 0
    num_digits = 0

    for digit in str(x_a):
        sum_digits += int(digit)
        num_digits += 1

    print("Сумма цифр:", sum_digits)
    print("Количество цифр:", num_digits)

# --------------------------------------------------------

if number == "B" or number == "b":
    x_b = int(input("Введите число:"))

    sum_digits_b = 0
    num_digits_b = 0

    for digit_b in str(x_b):
        sum_digits_b += int(digit_b)
        num_digits_b += 1

    if sum_digits_b % num_digits_b == 0:
        print("Да")
    else:
        print("Нет")

# --------------------------------------------------------

if number == "C" or number == "c":
    a_c = int(input("Введите первое число:"))
    b_c = int(input("Введите второе число:"))

    print(f"Красивые числа от {a_c} до {b_c}")

    if b_c > a_c:
        for num_c in range(a_c, b_c + 1):

            sum_digits_c = 0
            num_digits_c = 0

            for digit_c in str(num_c):
                sum_digits_c += int(digit_c)
                num_digits_c += 1

            if sum_digits_c % num_digits_c == 0:
                print(num_c)

    if a_c > b_c:
        for num_c in range(b_c, a_c + 1):

            sum_digits_c = 0
            num_digits_c = 0

            for digit_c in str(num_c):
                sum_digits_c += int(digit_c)
                num_digits_c += 1

            if sum_digits_c % num_digits_c == 0:
                print(num_c)

# --------------------------------------------------------

if number == "D" or number == "d":

    m = int(input("Введите число m:"))

    beatiful_count = 0
    last_beat_number = 1
    sum_digits_d = 0
    num_digits_d = 0
    num = 1

    while beatiful_count < m:
        sum_digits_d = 0
        for digit_d in str(num):
            sum_digits_d += int(digit_d)
            num_digits_d += 1

        num += 1

        if sum_digits_d % num_digits_d == 0:
            beatiful_count += 1
            last_beat_number = num

    print("m-ое красивое число:", last_beat_number)

# --------------------------------------------------------