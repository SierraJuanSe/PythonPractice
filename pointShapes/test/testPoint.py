import unittest
from pointShapes.src.point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 0)
        self.p2 = Point(-1, 0)

    def test_distance(self):
        self.assertEqual(2.0, self.p1.distance(self.p2), 'Should be 2.0')

    def test_inCircle(self):
        pass
