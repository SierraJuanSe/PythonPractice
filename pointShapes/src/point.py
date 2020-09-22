"""
Clase Punto
Metodos:
    distance: calcula la distancia entre el mismo y otro punto
    inCircle: comprueba si esta dentro de un circulo dado
"""


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** (1/2)

    def inCircle(self, circle):
        return circle.radius > self.distance(circle.points[0])
