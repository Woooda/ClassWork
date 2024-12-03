# Создайте список, содержащий только числа, делящиеся на 3 и 5, в пределах от 1 до 50.

n = int(input("Введите число N:"))

massiv = [i for i in range (n) if i % 3 == 0 and i % 5 == 0]

print(massiv)