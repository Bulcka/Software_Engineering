global result

def rectangle():
    a = float(input("Ширина "))
    b = float(input("Высота "))
    global result
    result = a*b
def triangle():
    a = float(input("Основание "))
    h = float(input("Высота"))
    global result
    result = 0.5 *a*h

if __name__ == '__main__':
    figure = input("1-прямоугольник 2- треугльник  ")
    if figure == "1":
        rectangle()
    elif figure == "2":
        triangle()
print(f"Площадь {result}")
    