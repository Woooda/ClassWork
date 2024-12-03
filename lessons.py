a = int(input())
b = int(input())

def GreatDivisor(a, b):
    while a != 0 and b!= 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    else:
        return (a + b)

divisor = GreatDivisor(a,b)
a = a // divisor
b = b // divisor

while b % 2 == 0:
    b //= 2

while b % 5 == 0:
    b //= 5

if b == 1:
    print("yes")
else:
    print("no")

