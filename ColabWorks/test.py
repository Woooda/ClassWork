#Разделение строки Напишите программу, которая принимает строку и разделяет её на список слов, которые содержат четное количество букв. Используйте генератор списка.

s = input()

newList = []
newS = ""
for i in s:
    if i != ' ':
        newS += i
    elif i == " ":
        newList += [newS]
        newS = ''
result = [x for x in newList if len(x) % 2 == 0]
print(result)


