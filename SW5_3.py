

import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_sides = [min(one), min(two), min(three)]
max_sides = [max(one), max(two), max(three)]

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area_min = triangle_area(*min_sides)
area_max = triangle_area(*max_sides)

print("Площадь треугольника (из минимальных):", round(area_min, 2))
print("Площадь треугольника (из максимальных):", round(area_max, 2))
