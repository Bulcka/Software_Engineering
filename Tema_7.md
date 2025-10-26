# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Лунегов Игорь Альбертович
- ИВТ-23-2 

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_1.png)



## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_2.png)



## Лабораторная работа №3
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_3.png)


  
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_4.png)



## Лабораторная работа №5
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    for line in f:
        print(line)
        
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_5.png)



## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нём тоже отображались.
```python
with open('input.txt') as f:
    for line in f:
        print(line)
        
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_6.png)



## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить, что изменённая вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_7.png)



## Лабораторная работа №8
### Выберите любую папку на своём компьютере, имеющую вложенные директории. Выведите на печать в терминал её содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f'Папка {root} содержит:')
        print(f'Директории: {", ".join(dirs) if dirs else "нет"}')
        print(f'Файлы: {", ".join(files) if files else "нет"}')
        print('-' * 40)

# Пример использования:
print_docs("C:/Users/qwerty/Desktop/another/test")
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_8.png)



## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: 

Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.   

Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
Проверьте работоспособность программы на своём наборе данных. 
```python
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
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_9.png)



## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 

• № — номер по порядку (от 1 до 300);
• Секунда — текущая секунда на вашем ПК;
• Микросекунда — текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды. 
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    
    for line in range(1, 301):
        now = datetime.datetime.now()
        writer.writerow([line, now.second, now.microsecond])
        time.sleep(0.01) 

print("Файл rows_300.csv успешно создан.")
```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/Lab7_10.png)



## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
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

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_1.png)


  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
def add_expense():
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")

    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{category};{amount};{description}\n")

def show_expenses():
    print("\nТекущие расходы:")
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                category, amount, description = line.strip().split(";")
                print(f"{category}: {amount} руб — {description}")
    except FileNotFoundError:
        print("Файл расходов пока не создан.")

while True:
    print("\nМеню:")
    print("1 — Добавить расход")
    print("2 — Показать все расходы")
    print("3 — Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Неверный выбор. Повторите ввод.")

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_21.png)
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_22.png)


  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
```python
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

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_3.png)


  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
```python
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

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_4.png)


  
## Самостоятельная работа №5
### Создать программу, которая считает количество уникальных слов в файле poem.txt и сохраняет результат в stats.txt.
```python
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

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_51.png)
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_7/pic/SW7_52.png)


  
