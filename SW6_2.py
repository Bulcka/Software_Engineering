def remove_first_occurrence(tpl, value):
    if value in tpl:
        index = tpl.index(value)
        return tpl[:index] + tpl[index+1:]
    else:
        return tpl

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
