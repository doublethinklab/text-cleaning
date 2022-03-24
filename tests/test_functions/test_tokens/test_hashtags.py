import unittest

from text_cleaning.functions.tokens import NormalizeHashtags


class TestNormalizeHashtags(unittest.TestCase):

    def setUp(self) -> None:
        self.clean = NormalizeHashtags()

    def test_case_1(self):
        tokens = ['#hashtag1', 'not_a_hashtag', '#weibostyle#']
        result = self.clean(tokens)
        expected = ['#hashtag1', 'not_a_hashtag', '#weibostyle']
        self.assertEqual(expected, result)
