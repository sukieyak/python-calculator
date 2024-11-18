import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add(self):
        self.assertEqual(self.calc.add(3, 7), 10)
    def test_add(self):
        self.assertEqual(self.calc.subtract(9, 1), 8)
    def test_add(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
    def test_add(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    def test_add(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
    def test_add(self):
        self.assertEqual(self.calc.divide(7, 3), 2)
    def test_add(self):
        self.assertEqual(self.calc.divide(9, 2), 4)
    def test_add(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)   
    def test_add(self):
        self.assertEqual(self.calc.modulo(3, 3), 0)   
    
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()