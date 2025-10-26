def longest_words(file):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        words = text.split()
    
    if not words:
        return "Файл пуст или содержит только пробелы."
    
    max_length = len(max(words, key=len))
    sought_words = [word for word in words if len(word) == max_length]
    
    
    return sought_words[0] if len(sought_words) == 1 else sought_words


print(longest_words('input.txt'))