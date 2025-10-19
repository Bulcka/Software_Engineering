def remove_duplicates(lst):
    seen = set()
    new_list = []
    for x in lst:
        if x not in seen:
            new_list.append(x)
            seen.add(x)
    removed = len(lst) - len(new_list)
    return new_list, removed

print(remove_duplicates([1, 2, 3, 1, 2, 3, 4]))
print(remove_duplicates([5, 5, 5, 5]))
print(remove_duplicates([1, 2, 3, 4, 5]))
