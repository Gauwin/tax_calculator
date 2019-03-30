import sys
sys.path.append('../')

import unittest
from main import zip_brackets

class TestZipBrackets(unittest.TestCase):

    def test_mismatch_brackets(self):
        self.assertEqual(None, zip_brackets((1000,), ()))

    def test_empty_bracket(self):
        self.assertEqual([], zip_brackets((), ()))

    def test_brackets(self):
        thresholds = (1000,)
        rates = (0.1,)
        expected = [{'threshold': 1000, 'rate': 0.1}]
        self.assertEqual(expected, zip_brackets(thresholds, rates))
