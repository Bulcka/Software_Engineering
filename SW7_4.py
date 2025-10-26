with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = f.read().split()

sentence = input("Введите предложение: ")
lower_sentence = sentence.lower()
result = list(sentence)

for banned in banned_words:
    start = 0
    while True:
        index = lower_sentence.find(banned, start)
        if index == -1:
            break
        for i in range(index, index + len(banned)):
            result[i] = '*'
        start = index + 1

print("\nРезультат:")
print("".join(result))
