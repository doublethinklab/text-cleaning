import unittest

from text_cleaning.functions.text import RemoveHtml


class TestRemoveHtml(unittest.TestCase):

    def setUp(self) -> None:
        self.clean = RemoveHtml()

    def test_case_1(self):
        text = '<a href=\'/n/Director_鹤唳云端\'>@Director_鹤唳云端</a>'
        result = self.clean(text)
        expected = ' @Director_鹤唳云端 '
        self.assertEqual(expected, result)
