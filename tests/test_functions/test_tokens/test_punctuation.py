import unittest

from text_cleaning.functions.tokens import RemovePunctuation


class TestRemovePunctuation(unittest.TestCase):

    def test_case_1(self):
        fn = RemovePunctuation()
        tokens = ['ti.dy', 'clean']
        result = fn(tokens)
        expected = ['tidy', 'clean']
        self.assertEqual(expected, result)
