import unittest

from text_cleaning.functions.text import TraditionalToSimplified


class TestTraditionalToSimplified(unittest.TestCase):

    def setUp(self):
        self.fn = TraditionalToSimplified()

    def test_case_1(self):
        text = '國家'
        result = self.fn(text)
        expected = '国家'
        self.assertEqual(expected, result)
