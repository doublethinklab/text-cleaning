import unittest

from text_cleaning import replacements as repl
from text_cleaning.functions.tokens import ReplaceNumbers, ReplaceTooManyNumbers


class TestReplaceNumbers(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceNumbers(
            split_replacement=True, only_numbers=False)

    def test_no_split_replacement_leaves_token_intact(self):
        fn = ReplaceNumbers(
            split_replacement=False,
            only_numbers=False)
        tokens = ['10days']
        result = fn(tokens)
        self.assertEqual([f'{repl.NUMBER}days'], result)

    def test_split_replacement_splits_token(self):
        fn = ReplaceNumbers(
            split_replacement=True,
            only_numbers=False)
        tokens = ['10days']
        result = fn(tokens)
        self.assertEqual([repl.NUMBER, 'days'], result)

    def test_only_numbers_replaces_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=True)
        tokens = ['10']
        result = fn(tokens)
        self.assertEqual([repl.NUMBER], result)

    def test_not_only_numbers_replaces_when_not_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=False)
        text = ['10days']
        result = fn(text)
        self.assertEqual([f'{repl.NUMBER}days'], result)

    def test_case_4(self):
        tokens = ['123', '123a', 'a123', 'a123b']
        result = self.fn(tokens)
        # first token just maps to NUMBER
        # second splits as NUMBER and a
        # third as a and NUMBER
        # fourth as a and NUMBER and b
        expected = [
            repl.NUMBER, repl.NUMBER, 'a', 'a', repl.NUMBER, 'a',
            repl.NUMBER, 'b']
        self.assertEqual(expected, result)
