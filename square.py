import unittest

class Testcircle(unittest.TestCase):
    def testPerimetr(self):
        self.assertEqual(perimeter(12),48)
        self.assertEqual(perimeter(100000), 10000*4)
    def testPerimetr_1(self):
        self.assertEqual(perimeter(12),48)
    def testArea(self):
        self.assertEqual(area(2**0.5), 2)
    def testArea(self):
        self.assertEqual(area(100000), 10000000 ** 2)


def area(a):
    return a * a
def perimeter(a):   
    return 4 * a
