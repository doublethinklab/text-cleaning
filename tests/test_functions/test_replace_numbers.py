import unittest

from text_cleaning.chars import NUM
from text_cleaning.functions import ReplaceNumbers


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
        self.assertEqual(['NUMdays'], result)

    def test_split_replacement_splits_token(self):
        fn = ReplaceNumbers(
            split_replacement=True,
            only_numbers=False)
        tokens = ['10days']
        result = fn(tokens)
        self.assertEqual(['NUM', 'days'], result)

    def test_only_numbers_replaces_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=True)
        tokens = ['10']
        result = fn(tokens)
        self.assertEqual(['NUM'], result)

    def test_not_only_numbers_replaces_when_not_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=False)
        text = ['10days']
        result = fn(text)
        self.assertEqual(['NUMdays'], result)

    def test_case_1(self):
        text = 'Iam10yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        text = 'Iam100000000000000yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_3(self):
        text = 'Iam０１yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_4(self):
        tokens = ['123', '123a', 'a123', 'a123b']
        result = self.fn(tokens)
        expected = [NUM, NUM, 'a', 'a', NUM, 'a', NUM, 'b']
        self.assertEqual(expected, result)
