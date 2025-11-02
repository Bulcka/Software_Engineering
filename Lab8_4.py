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
