with open("poem.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

for ch in ",.!?;:-\n":
    text = text.replace(ch, " ")

words = [w for w in text.split() if w.isalpha()]
unique_words = set(words)

with open("stats.txt", "w", encoding="utf-8") as f:
    f.write(f"Всего слов: {len(words)}\n")
    f.write(f"Уникальных слов: {len(unique_words)}\n")
    f.write("Список уникальных слов:\n")
    f.write(", ".join(sorted(unique_words)))

print("Результат сохранён в файл stats.txt")
