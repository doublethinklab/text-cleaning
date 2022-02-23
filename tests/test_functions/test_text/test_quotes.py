import unittest

from text_cleaning.functions.text.quotes import ReplaceQuotes


class TestReplaceQuotes(unittest.TestCase):

    def test_case_1(self):
        text = 'He said "get lost" and then disappeared.'
        result = ReplaceQuotes(replacement='QUOTEPLACEHOLDER')(text)
        expected = 'He said QUOTEPLACEHOLDER and then disappeared.'
        self.assertEqual(expected, result)
