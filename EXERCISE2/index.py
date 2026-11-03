def second_largest(numbers):
    largest = None
    second_largest = None

    for number in numbers:
        if number == largest:
            continue 
    
        if largest is None or number > largest:
            second_largest = largest
            largest = number

        elif second_largest is None or number > second_largest:
            second_largest = number
    
    return second_largest

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4]))
print(second_largest([-5, -2, -8, -3]))
        