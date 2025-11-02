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
