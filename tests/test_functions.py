import unittest

from text_cleaning.functions import *





class TestReplaceUrls(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceUrls()

    def test_case_1(self):
        tokens = ['Some', 'text', 'https://docs.python.org/3/howto/regex.html']
        result = self.fn(tokens)
        expected = ['Some', 'text', f'{URL}']
        self.assertEqual(expected, result)



