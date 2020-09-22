import math
from pointShapes.src.shape import Shape


class Circle(Shape):
    def __init__(self, radius, points):
        Shape.__init__(points)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
