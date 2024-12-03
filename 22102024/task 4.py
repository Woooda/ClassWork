# Создайте список, содержащий удвоенные значения всех четных чисел от 0 до 9.

n = int(input("Введите число N:"))

massiv = [i*2 for i in range(n) if i % 2 == 0 ]

print(massiv)