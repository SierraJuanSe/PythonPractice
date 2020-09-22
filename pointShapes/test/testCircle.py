
import unittest
from pointShapes.src.circle import Circle
from pointShapes.src.point import Point


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(2, [Point(0, 0)])

    def test_Area(self):
        self.assertAlmostEqual(
            12.57, self.circle.area(), msg="Should be almost 12.57")

    def test_Permeter(self):
        self.assertAlmostEqual(
            12.57, self.circle.perimeter(), msg="Should be almost 12.57")
