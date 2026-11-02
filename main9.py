def first_duplicate(numbers):
    seen_number = []
    for number in numbers:
        if number in seen_number:
            return number
    
        seen_number.append(number)
    return None


print(first_duplicate([4, 7, 2, 7, 5, 4]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([5, 5, 3]))