a = int(input())

digit = 0

summa = 0

while a != 0:
    digit = a % 10
    summa += digit
    a = a // 10

print(summa)