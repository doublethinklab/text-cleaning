import unittest

from text_cleaning import languages as lang
from text_cleaning.functions.text import RemoveGarbage


class TestRemoveGarbage(unittest.TestCase):

    def test_case_1(self):
        remove = RemoveGarbage()
        text = '◆外交部abc123.?'
        result = remove(text)
        expected = '外交部abc123.?'
        self.assertEqual(expected, result)

    def test_case_2(self):
        remove = RemoveGarbage()
        text = 'Text https://something.com 123  goes◆ here.'
        result = remove(text)
        expected = 'Text https://something.com 123  goes here.'
        self.assertEqual(expected, result)

    def test_chinese_removed_when_not_ordered(self):
        remove = RemoveGarbage(languages=[lang.en])
        text = '◆外交部abc123.?'
        result = remove(text)
        expected = 'abc123.?'
        self.assertEqual(expected, result)

    def test_hyphen_not_removed(self):
        remove = RemoveGarbage(languages=[lang.en])
        text = '24 provincial-level regions across China report zero new ' \
               'cases of #COVID19 infection on Monday. https://t.co/SALtWuqFJP'
        result = remove(text)
        expected = text
        self.assertEqual(expected, result)
