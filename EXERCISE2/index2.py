def move_zeros(numbers):
    insert_pos = 0

    for number in numbers:
        if number != 0:
            numbers[insert_pos] = number
            insert_pos += 1

    while insert_pos < (len(numbers)):
        numbers[insert_pos] = 0
        insert_pos += 1

    return numbers

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([4, 0, 5, 0, 2]))
print(move_zeros([1, 2, 3]))