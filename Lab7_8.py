import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f'Папка {root} содержит:')
        print(f'Директории: {", ".join(dirs) if dirs else "нет"}')
        print(f'Файлы: {", ".join(files) if files else "нет"}')
        print('-' * 40)

# Пример использования:
print_docs("C:/Users/qwerty/Desktop/another/test")