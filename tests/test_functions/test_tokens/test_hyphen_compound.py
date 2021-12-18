import unittest

from text_cleaning.functions.tokens import ReplaceHyphenCompoundWithSpace


class TestReplaceHyphenCompoundWithSpace(unittest.TestCase):

    def test_case_1(self):
        fn = ReplaceHyphenCompoundWithSpace()
        tokens = ['hyphen-compound', 'something']
        result = fn(tokens)
        expected = ['hyphen', 'compound', 'something']
        self.assertEqual(expected, result)
