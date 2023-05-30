import unittest
import calc
"""
assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(a)
assertFalse(a)
assertRaises(exc, cal)
assertAlmostEqual(a, b)
assertNotAlmostEqual(a, b)
"""


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(2, 1), 1)
        self.assertEqual(calc.subtract(1, -1), 2)


    def test_multiply(self):
        self.assertEqual(calc.multiply(1, -1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(0, -1), 0)
        self.assertEqual(calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(2, -2), -1)
        self.assertEqual(calc.divide(-2, -2), 1)
        self.assertEqual(calc.divide(4, -1), -4)

        # self.assertRaises(ValueError, calc.divide, 10 , 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()