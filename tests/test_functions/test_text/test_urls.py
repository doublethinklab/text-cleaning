import unittest

from text_cleaning import replacements
from text_cleaning.functions.text import RemoveUrls, ReplaceUrls


class TestRemoveUrls(unittest.TestCase):

    def setUp(self) -> None:
        self.clean = RemoveUrls()

    def test_case_1(self):
        text = '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客 ' \
               'https://t.co/KAajTmJG04'
        result = self.clean(text)
        expected = '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客'
        self.assertEqual(expected, result)


class TestReplaceUrls(unittest.TestCase):

    def setUp(self) -> None:
        self.clean = ReplaceUrls()

    def test_case_1(self):
        text = '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客 ' \
               'https://t.co/KAajTmJG04'
        result = self.clean(text)
        expected = '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客 %s' \
                   % replacements.URL
        self.assertEqual(expected, result)
