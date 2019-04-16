from unittest import TestCase
from Excercise3 import isMatch

class TestIsMatch(TestCase):
    def test_isMatch_false(self):
        self.assertFalse(isMatch("aa","?b"))

    def test_isMatch_true(self):
        self.assertTrue(isMatch("aa","*"))
