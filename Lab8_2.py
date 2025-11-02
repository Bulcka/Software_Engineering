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
