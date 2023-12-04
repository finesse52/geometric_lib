import math
import unittest

class TestCircle(unittest.TestCase):
    def testPer(self):
        self.assertEqual(perimeter(1/(2*math.pi)), 1)
        class TestCircle(unittest.TestCase):
    def testPer(self):
        self.assertEqual(perimeter(2/(2*math.pi)), 2)

    def testArea(self):
        self.assertEqual(area(2 / (math.pi ** 0.5)), float(4))
            def testArea(self):
        self.assertEqual(area(4 / (math.pi ** 0.5)), float(2))
def perimeter(r):
    return 2*math.pi * r
def area(r):
    return math.pi * r * r

