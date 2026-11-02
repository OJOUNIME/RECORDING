def has_duplicates(numbers):
    seen_number = []

    for number in numbers:
        if number in seen_number:
            return True
        seen_number.append(number)
    return False

print(has_duplicates([1, 2, 3, 2]))
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([]))