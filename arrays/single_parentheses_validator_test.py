import unittest

from arrays import single_parentheses_validator as validator


class MyTest(unittest.TestCase):
    def valid(self):
        self.assertEqual(validator.validate("()"), True)

    def not_valid(self):
        self.assertEqual(validator.validate("((("), True)

