

def make_custom_set(lst):
    result = set()
    for num in set(lst):
        count = lst.count(num)
        result.add(num)
        for i in range(2, count + 1):
            result.add(str(num) * i)
    return result

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(make_custom_set(list_1))
print(make_custom_set(list_2))
print(make_custom_set(list_3))
