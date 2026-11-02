def move_zeros(numbers):
    non_zeros = []
    zeros = []

    for number in numbers:
        if number == 0:
            zeros.append(number)
        else:
            non_zeros.append(number)
    return non_zeros + zeros

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))