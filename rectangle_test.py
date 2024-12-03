import unittest
from points import Point
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 1)
        self.p2 = Point(4, 5)
        self.rect = Rectangle(1, 1, 4, 5)

    def test_from_points(self):
        rect = Rectangle.from_points((self.p1, self.p2))
        self.assertEqual(rect.left, 1)
        self.assertEqual(rect.right, 4)
        self.assertEqual(rect.bottom, 1)
        self.assertEqual(rect.top, 5)

    def test_virtual_properties(self):
        self.assertEqual(self.rect.left, 1)
        self.assertEqual(self.rect.right, 4)
        self.assertEqual(self.rect.bottom, 1)
        self.assertEqual(self.rect.top, 5)
        self.assertEqual(self.rect.width, 3)
        self.assertEqual(self.rect.height, 4)
        self.assertEqual(self.rect.topleft, Point(1, 5))
        self.assertEqual(self.rect.bottomright, Point(4, 1))

    def test_center(self):
        self.assertEqual(self.rect.center, Point(2.5, 3))

    def make4(self):
        center = self.center  # Zmiana z wywołania funkcji na dostęp do właściwości
        r1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        r3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        return (r1, r2, r3, r4)


if __name__ == "__main__":
    unittest.main()
