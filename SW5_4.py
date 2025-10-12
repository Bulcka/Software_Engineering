

lists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

for i, marks in enumerate(lists, start=1):
    updated = [4 if m == 3 else m for m in marks if m != 2]
    print(f"Обновлённый список {i}:", updated)
