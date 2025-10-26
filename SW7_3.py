with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)

letters = sum(c.isalpha() for c in text)
words = len(text.split())
lines_count = len(lines)

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")
