import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3)

if __name__ == "__main__":
    unittest.main()
