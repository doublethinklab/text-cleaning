import unittest

from text_cleaning.functions.tokens import RemoveTooShortTokens


class TestRemoveTooShortTokens(unittest.TestCase):

    def test_case_1(self):
        fn = RemoveTooShortTokens()
        tokens = ['i', 'am', 'b', 'what']
        result = fn(tokens)
        expected = ['i', 'am', 'what']
        self.assertEqual(expected, result)
