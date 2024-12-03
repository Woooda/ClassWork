# Задача: Напишите генератор, который возвращает только четные числа от 1 до N, а также используйте list comprehension для создания списка четных чисел.

num = int(input("Введите число N:"))
massiv = [i for i in range (num) if i % 2 == 0]
print(massiv)