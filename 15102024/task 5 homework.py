
# Введите массив чисел и переверните его (отразите в обратном порядке).
# Введите массив чисел и удалите все отрицательные элементы.
# Введите массив чисел и посчитайте количество положительных элементов.
# Введите массив чисел и найдите произведение всех элементов.
# Введите массив чисел и умножьте каждый элемент массива на 2.
# Введите массив чисел и сдвиньте его элементы на одну позицию вправо.


count_number = int(input("Сколько чисел вы планируете вводить, гопсодин:"))

massiv_1 = [0] * count_number
print(massiv_1)

for i in range(count_number):
    massiv_1[i] = int(input("Введите число, госgодин:"))
print(massiv_1)


for i in range(0, count_number // 2):
    massiv_1[i], massiv_1[len(massiv_1) - i - 1] = massiv_1[len(massiv_1) - i - 1], massiv_1[i]
    print(massiv_1)

print(massiv_1)