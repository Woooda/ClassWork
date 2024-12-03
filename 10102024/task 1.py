a = int(input("Введите кол-во элементов:"))

list_number = [0] * a

print(list_number)

for i in range(len(list_number)):
    list_number[i] = int(input("Введите элемент массива:"))

print(list_number)

for i in range(0, len(list_number) // 2):
    list_number[i], list_number[len(list_number) - i - 1] = list_number[len(list_number) - i - 1], list_number[i]

print(list_number)

for i in range(len(list_number)):
    list_number[i] += 1

print(list_number)









