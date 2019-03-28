import sys
sys.path.append('..')

import unittest
from main import calculate_tax

class TestTaxCalculator(unittest.TestCase):

    def test_below_threshold(self):
        income = 100
        rates = [{'threshold': 1000, 'rate': 0.1}]
        (after_tax, taxed) = calculate_tax(income, rates)
        self.assertEqual(income, after_tax)
        self.assertEqual(0, taxed)

    def test_above_first_threshold(self):
        income = 2000
        rates = [{'threshold': 1000, 'rate': 0.1}]
        (after_tax, taxed) = calculate_tax(income, rates)
        self.assertEqual(1900, after_tax)
        self.assertEqual(100, taxed)

    def test_above_multiple_thresholds(self):
        income = 2000
        rates = [{'threshold': 1000, 'rate': 0.1}, {'threshold': 1500, 'rate': 0.2}]
        (after_tax, taxed) = calculate_tax(income, rates)
        self.assertEqual(1850, after_tax)
        self.assertEqual(150, taxed)

if __name__ == '__main__':
    unittest.main()
