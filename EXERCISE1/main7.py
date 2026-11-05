def reverse_list(items):
    reversed_items = []
    for i in range(len(items) -1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items

print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))