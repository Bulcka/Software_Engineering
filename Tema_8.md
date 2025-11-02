# ТЕМА 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Лунегов Игорь Альбертович
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 |  |  |
| Задание 7 |  |  |
| Задание 8 |  |  |
| Задание 9 |  |  |
| Задание 10 |  |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс "Car" с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")

```

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину "поехать". Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

    def drive(self):
        # Метод, выводящий сообщение о движении автомобиля
        print(f"Driving the {self.make} {self.model}")

# Создание объекта и вызов метода
my_car = Car("Toyota", "Corolla")
my_car.drive()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/Lab8_2.png)



## Лабораторная работа №3
###     Создайте новый класс "ElectricCar" с методом "charge" и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом зарядиться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 
```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

    def drive(self):
        # Метод, выводящий сообщение о движении автомобиля
        print(f"Driving the {self.make} {self.model}")

# Создание объекта и вызов метода
my_car = Car("Toyota", "Corolla")
my_car.drive()

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # Вызов конструктора родительского класса
        self.battery_capacity = battery_capacity  # Ёмкость батареи

    def charge(self):
        # Метод, выводящий сообщение о зарядке автомобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создание объекта и вызов методов родительского и собственного класса
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/Lab8_3.png)


  
## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:
    def __init__(self, make, model):
        self.__make = make  
        self.__model = model  

    def drive(self):
        # Метод, выводящий информацию о движении автомобиля
        print(f"Driving the {self.__make} {self.__model}")

# Создание объекта класса Car
my_car = Car("Toyota", "Corolla")

# Доступ к приватному атрибуту через внутреннее имя
print(my_car._Car__make)
# print(my_car.__model)  # Ошибка! Прямой доступ невозможен

# Вызов метода drive()
my_car.drive()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/Lab8_4.png)



## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс "Shape", а также еще два класса "Rectangle" и "Circle". Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Shape:
    def area(self):
        # Базовый метод для вычисления площади (переопределяется в подклассах)
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Ширина прямоугольника
        self.height = height  # Высота прямоугольника

    def area(self):
        # Вычисление площади прямоугольника
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Радиус круга

    def area(self):
        # Вычисление площади круга
        return 3.14 * self.radius * self.radius

# Создание списка фигур и вывод их площадей
figures = [Rectangle(4, 5), Circle(3)]
for figure in figures:
    print(figure.area())

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/Lab8_5.png)



## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author 


my_book = Book("1984", "George Orwell")


print(f"Book title: {my_book.title}")
print(f"Author: {my_book.author}")

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/SW8_1.png)


  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year 
        self.pages = pages 

    def description(self):
        print(f"'{self.title}' by {self.author}, {self.year} ({self.pages} pages)")

my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)
my_book.description()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/SW8_2.png)


  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
from SW8_2 import Book
class EBook(Book):
    def __init__(self, title, author, year, pages, file_size):
        super().__init__(title, author, year, pages) 
        self.file_size = file_size  

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size} MB)...")


ebook = EBook("Digital Fortress", "Dan Brown", 1998, 356, 5)
ebook.description()
ebook.download()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/SW8_3.png)


  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
    def __init__(self, title, author, year):
        self.__title = title    
        self.__author = author  
        self.__year = year      

    def info(self):
       
        print(f"'{self.__title}' by {self.__author}, {self.__year}")

    def set_year(self, new_year):
        
        self.__year = new_year


book = Book("Fahrenheit 451", "Ray Bradbury", 1953)
book.info()
book.set_year(1967)
book.info()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/SW8_4.png)


  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли
```python
class Publication:
    def info(self):
        pass 

class Book(Publication):
    def info(self):
        print("This is a printed book.")

class Magazine(Publication):
    def info(self):
        print("This is a monthly magazine.")

class Newspaper(Publication):
    def info(self):
        print("This is a daily newspaper.")


publications = [Book(), Magazine(), Newspaper()]
for p in publications:
    p.info()

```
### Результат.
![Меню](https://github.com/Bulcka/Software_Engineering/blob/Тема_8/pic/SW8_5.png)


