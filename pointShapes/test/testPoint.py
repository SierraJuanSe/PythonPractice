import unittest

from pointShapes.src.point import Point
from pointShapes.src.circle import Circle


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 0)
        self.p2 = Point(-1, 0)

    def test_distance(self):
        self.assertEqual(2.0, self.p1.distance(self.p2), 'Should be 2.0')

    def test_inCircle(self):
        point = Point(1, 1)
        circle = Circle(2, [Point(0, 0)])
        self.assertTrue(point.inCircle(circle), msg="Should be True")
