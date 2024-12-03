# Разбор ДЗ

# Создайте список, содержащий только простые числа от 100 до 200.

for i in range(1,11):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
number = [i for i in range(100,201) if all(i % j !=0 for j in range(2, i))]
print(number)