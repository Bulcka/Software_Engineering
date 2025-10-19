def extract_between(tpl, element):
    if element not in tpl:
        return ()
    first_index = tpl.index(element)
    if tpl.count(element) == 1:
        return tpl[first_index:]
    else:
        second_index = tpl.index(element, first_index + 1)
        return tpl[first_index:second_index + 1]

print(extract_between((1, 2, 3), 8))
print(extract_between((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(extract_between((1, 2, 8, 5, 1, 2, 9), 8))
