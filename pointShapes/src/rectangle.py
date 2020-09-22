from pointShapes.src.shape import Shape


class Rectangle(Shape):
    def __init__(self, points):
        super().__init__(points)

    def area(self):
        return self.points[0].distance(self.points[1]) * self.points[1].distance(self.points[2])

    def perimeter(self):
        return (self.points[0].distance(self.points[1]) * 2) + (self.points[1].distance(self.points[2]) * 2)
