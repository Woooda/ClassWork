# Создайте список, содержащий квадраты чисел от 1 до 10.

n = int(input("Введите число N:"))
massiv = [i ** 2 for i in range(n)]

print(massiv)