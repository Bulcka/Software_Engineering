with open("article.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

for ch in ",.!?;:-()[]\"'\n":
    text = text.replace(ch, " ")

words = [w for w in text.split() if w.isalpha()]
word_count = len(words)

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

most_common_word = None
max_count = 0
for word, count in freq.items():
    if count > max_count:
        max_count = count
        most_common_word = word

print(f"Количество слов в статье: {word_count}")
print(f"Самое частое слово: '{most_common_word}' (встречается {max_count} раз)")
