a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Числа харшад от", a, "до", b, ":")

for num in range(a, b + 1):
  sum_digits = 0
  for digit in str(num):
    sum_digits += int(digit)
  if num % sum_digits == 0:
    print(num)
