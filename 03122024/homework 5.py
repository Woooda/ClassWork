# 5. Создайте список, содержащий остатки от деления чисел от 1 до 20 на 3.
itogo = [x % 3 for x in range(1, 21)]
print("Остатки от деления чисел от 1 до 20 на 3:", itogo)