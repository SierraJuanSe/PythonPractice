import math
from pointShapes.src.shape import Shape


class Triangle(Shape):
    def __init__(self, points):
        super().__init__(points)

    def type(self):
        sides = [
            self.points[0].distance(self.points[1]),
            self.points[1].distance(self.points[2]),
            self.points[2].distance(self.points[0])
        ]

        ab = abs(sides[0] - sides[1]) < 0.01
        ac = abs(sides[0] - sides[2]) < 0.01
        bc = abs(sides[1] - sides[2]) < 0.01

        if ab and ac:
            return "equilateral"
        elif ab or ac or bc:
            return "isosceles"
        else:
            return "scalene"

    def area(self):
        s = self.perimeter() / 2
        return (s
                * (s - self.points[0].distance(self.points[1]))
                * (s - self.points[1].distance(self.points[2]))
                * (s - self.points[2].distance(self.points[0])))

    def perimeter(self):
        return (self.points[0].distance(self.points[1])
                + self.points[1].distance(self.points[2])
                + self.points[2].distance(self.points[0]))
