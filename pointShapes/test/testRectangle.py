import unittest

from pointShapes.src.point import Point
from pointShapes.src.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle([
            Point(-1, 0),
            Point(-1, 1),
            Point(1, 1),
            Point(1, 0)
        ])

    def test_Area(self):
        self.assertAlmostEqual(
            2.0, self.rectangle.area(), msg="Should be 2", delta=0.01)

    def test_Perimeter(self):
        self.assertAlmostEqual(
            6.0, self.rectangle.perimeter(), msg="Should be 6", delta=0.01)
