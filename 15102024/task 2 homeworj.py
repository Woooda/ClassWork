# Введите массив чисел и найдите сумму всех элементов.
# Введите массив чисел и найдите минимальный элемент массива.
# Введите массив чисел и найдите максимальный элемент массива.
# Введите массив чисел и посчитайте количество четных элементов.
# Введите массив чисел и переверните его (отразите в обратном порядке).
# Введите массив чисел и удалите все отрицательные элементы.
# Введите массив чисел и посчитайте количество положительных элементов.
# Введите массив чисел и найдите произведение всех элементов.
# Введите массив чисел и умножьте каждый элемент массива на 2.
# Введите массив чисел и сдвиньте его элементы на одну позицию вправо.

minimum = 10 ** 10
count_nubmer = int(input("Сколько чисел вы планируете вводить, гопсодин:"))

for i in range(count_nubmer):
    result = int(input("Введите число, госgодин:"))
    if result < minimum:
        minimum = result