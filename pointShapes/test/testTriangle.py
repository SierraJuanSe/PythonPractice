import unittest

from pointShapes.src.point import Point
from pointShapes.src.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.equilateral = Triangle([Point(0, 0), Point(2, 0), Point(1, 1.73)])
        self.isosceles = Triangle([Point(0, 0), Point(2, 0), Point(1, 2)])
        self.scalene = Triangle([Point(0, 0), Point(3, 0), Point(1, 2)])

    def test_TriangleType(self):
        self.assertMultiLineEqual(
            "equilateral", self.equilateral.type(), msg="Should be equilateral")
        self.assertMultiLineEqual(
            "isosceles", self.isosceles.type(), msg="Should be isosceles")
        self.assertMultiLineEqual(
            "scalene", self.scalene.type(), msg="Should be scalene")

    def test_Area(self):
        self.assertAlmostEqual(
            1.73, self.equilateral.area(), msg="Should almost be 1.73", delta=0.01)
        self.assertAlmostEqual(
            2, self.isosceles.area(), msg="Should almost be 2", delta=0.01)
        self.assertAlmostEqual(
            3, self.scalene.area(), msg="Should almost be 3", delta=0.01)

    def test_Perimeter(self):
        self.assertAlmostEqual(
            6, self.equilateral.perimeter(), msg="Should almost be 6", delta=0.01)
        self.assertAlmostEqual(
            6.48, self.isosceles.perimeter(), msg="Should almost be 6.48", delta=0.01)
        self.assertAlmostEqual(
            8.07, self.scalene.perimeter(), msg="Should almost be 8.07", delta=0.01)
