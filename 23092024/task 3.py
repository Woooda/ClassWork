number_orig = int(input())

number_copy = number_orig
digit = 0
summa = 0
proud = 1

while number_orig != 0:
    digit = number_orig % 10
    summa += digit
    number_orig = number_orig // 10


if number_copy % summa == 0:
    print("Да")
else:
    print("Нет")