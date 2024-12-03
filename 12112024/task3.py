numbers = [1,2,-3,-4,5,6,-7,-8,9,10]

good_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        numbers[i] *= -1

    else:
        numbers[i] *= -1

print(numbers)