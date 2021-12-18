import unittest

from text_cleaning import replacements as repl
from text_cleaning.functions.tokens import ReplaceUrls


class TestReplaceUrls(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceUrls()

    def test_case_1(self):
        tokens = ['Some', 'text', 'https://docs.python.org/3/howto/regex.html']
        result = self.fn(tokens)
        expected = ['Some', 'text', repl.URL]
        self.assertEqual(expected, result)
