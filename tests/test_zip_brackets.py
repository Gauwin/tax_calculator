import sys
sys.path.append('../')

import unittest
from generate_brackets import generate_brackets

class TestZipBrackets(unittest.TestCase):

    def test_mismatch_brackets(self):
        self.assertEqual(None, generate_brackets((1000,), ()))

    def test_empty_bracket(self):
        self.assertEqual([], generate_brackets((), ()))

    def test_brackets(self):
        thresholds = (1000,)
        rates = (0.1,)
        expected = [{'threshold': 1000, 'rate': 0.1}]
        self.assertEqual(expected, generate_brackets(thresholds, rates))
