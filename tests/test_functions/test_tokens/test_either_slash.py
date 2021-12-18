import unittest

from text_cleaning.functions.tokens import ReplaceEitherSlashWithSpace


class TestReplaceEitherSlashWithSpace(unittest.TestCase):

    def test_case_1(self):
        fn = ReplaceEitherSlashWithSpace()
        tokens = ['and/or', 'something']
        result = fn(tokens)
        expected = ['and', 'or', 'something']
        self.assertEqual(expected, result)
