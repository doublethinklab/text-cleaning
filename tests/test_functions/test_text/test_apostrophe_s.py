import unittest

from text_cleaning.functions.text import RemoveTrailingApostropheS


class TestRemoveTrailingApostropheS(unittest.TestCase):

    def test_case_1(self):
        remove = RemoveTrailingApostropheS()
        text = "It's just not it."
        result = remove(text)
        expected = 'It just not it.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        remove = RemoveTrailingApostropheS()
        text = "It's Tim's."
        result = remove(text)
        expected = 'It Tim.'
        self.assertEqual(expected, result)
