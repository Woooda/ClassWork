# 6. Создайте список, содержащий только числа от 1 до 50, которые делятся на 5.
itogo = [x for x in range(1, 51) if x % 5 == 0]
print("Числа от 1 до 50, которые делятся на 5:", itogo)