import sys
sys.path.append("..")

import unittest
from calculate_tax import calculate_flat_rate_tax

class TestFlatRateTaxCalculator(unittest.TestCase):

    def test_below_threshold(self):
        income = 100
        brackets = [{'threshold': 1000, 'rate': 0.1}]
        (after_tax, taxed) = calculate_flat_rate_tax(income, brackets)
        self.assertEqual(income, after_tax)
        self.assertEqual(0, taxed)

    def test_on_threshold(self):
        income = 2000
        brackets = [{'threshold': 1000, 'rate': 0.1}, {'threshold': 2000, 'rate': 0.2}]
        (after_tax, taxed) = calculate_flat_rate_tax(income, brackets)
        self.assertEqual(1800, after_tax)
        self.assertEqual(200, taxed)

    def test_above_threshold(self):
        income = 1500
        brackets = [{'threshold': 1000, 'rate': 0.1}, {'threshold': 2000, 'rate': 0.2}]
        (after_tax, taxed) = calculate_flat_rate_tax(income, brackets)
        self.assertEqual(1350, after_tax)
        self.assertEqual(150, taxed)

    if __name__ == '__main__':
        unittest.main()
