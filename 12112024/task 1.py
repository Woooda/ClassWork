list_numbers = [1, -4, 7, 12]

list_numbers_greate = []

for i in range(len(list_numbers)):
    if list_numbers[i] > 0:
        list_numbers_greate += [list_numbers[i]]

summa = 0

for i in list_numbers_greate:
    summa += i

print(summa)