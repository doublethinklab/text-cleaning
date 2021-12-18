import unittest

from text_cleaning import replacements as repl
from text_cleaning.functions.text import ReplaceNumbers


class TestReplaceNumbers(unittest.TestCase):

    def test_case_1(self):
        fn = ReplaceNumbers()
        text = 'Iam10yearsexperienced.'
        result = fn(text)
        expected = f'Iam10yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        fn = ReplaceNumbers()
        text = 'Iam100000000000000yearsexperienced.'
        result = fn(text)
        expected = f'Iam{repl.NUMBER}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_3(self):
        fn = ReplaceNumbers()
        text = 'Iam０１１yearsexperienced.'
        result = fn(text)
        expected = f'Iam{repl.NUMBER}yearsexperienced.'
        self.assertEqual(expected, result)
