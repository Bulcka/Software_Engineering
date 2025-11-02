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
