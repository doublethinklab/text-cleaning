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
        remove = RemoveGarbage(languages=['en_US'])
        text = '◆外交部abc123.?'
        result = remove(text)
        expected = 'abc123.?'
        self.assertEqual(expected, result)

    def test_spanish_case(self):
        remove = RemoveGarbage(languages=['es_ES'])
        text = '◆外交部abc123áéíóúñüÁÉÍÓÚÑÜ'
        result = remove(text)
        expected = 'abc123áéíóúñüÁÉÍÓÚÑÜ'
        self.assertEqual(expected, result)

    def test_italian_case(self):
        remove = RemoveGarbage(languages=['it_IT'])
        text = '◆そういう外交部abc123ÀàÈèÉéÌìÒòÙù'
        result = remove(text)
        expected = 'abc123ÀàÈèÉéÌìÒòÙù'
        self.assertEqual(expected, result)

    def test_arabic_case(self):
        remove = RemoveGarbage(languages=['ar_AE'])
        text = '◆そういう外交部abc123مراسل بي بي سي'
        result = remove(text)
        expected = '123مراسل بي بي سي'
        self.assertEqual(expected, result)

    def test_french_case(self):
        remove = RemoveGarbage(languages=['fr_FR'])
        text = '◆そういう外交部abc123ÀÂÆÇÈÉÊËÎÏÔÙÛÜŸŒœàâæçèéêëîïôùûüÿ'
        result = remove(text)
        expected = 'abc123ÀÂÆÇÈÉÊËÎÏÔÙÛÜŸŒœàâæçèéêëîïôùûüÿ'
        self.assertEqual(expected, result)

    def test_hyphen_not_removed(self):
        remove = RemoveGarbage(languages=[lang.en_us])
        text = '24 provincial-level regions across China report zero new ' \
               'cases of #COVID19 infection on Monday. https://t.co/SALtWuqFJP'
        result = remove(text)
        expected = text
        self.assertEqual(expected, result)
