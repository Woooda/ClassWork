a = int(input())

digit = 0

proud = 1

while a != 0:
    digit = a % 10
    proud *= digit
    a = a // 10
print(proud)