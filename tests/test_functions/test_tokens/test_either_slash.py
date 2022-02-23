import unittest

from data_structures.nlp import Token

from text_cleaning.functions.tokens import ReplaceEitherSlashWithSpace


class TestReplaceEitherSlashWithSpace(unittest.TestCase):

    def test_case_1(self):
        fn = ReplaceEitherSlashWithSpace()
        tokens = ['and/or', 'something']
        result = fn(tokens)
        expected = ['and', 'or', 'something']
        self.assertEqual(expected, result)

    def test_double_spaces_also_removed(self):
        # NOTE: this test case isn't testing what it's supposed to
        # TODO: figure out where the problem is actually coming from
        fn = ReplaceEitherSlashWithSpace()
        tokens = [
            Token('this and/or', is_entity=True),
            Token('something'),
        ]
        result = fn(tokens)
        expected = [
            'this and or',
            'something',
        ]
        self.assertEqual(expected, result)
