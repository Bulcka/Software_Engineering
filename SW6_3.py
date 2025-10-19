def top_three_digits(s):
    counts = {int(ch): s.count(ch) for ch in set(s)}
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    top3 = dict(sorted(sorted_items[:3]))
    return top3

seq = "12334555999111222333388888"
result = top_three_digits(seq)
print(result)
