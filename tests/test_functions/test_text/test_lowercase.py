import unittest

from text_cleaning.functions.text import LowerCase


class TestLowerCase(unittest.TestCase):

    def test_case_1(self):
        fn = LowerCase()
        text = 'SOME TEXT'
        result = fn(text)
        expected = 'some text'
        self.assertEqual(expected, result)
