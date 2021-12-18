import unittest

from text_cleaning.functions.text import RemovePunctuation


class TestRemovePunctuation(unittest.TestCase):

    def setUp(self) -> None:
        self.fn = RemovePunctuation()

    def test_english_punctuation(self):
        text = 'I, the "author," disapprove.'
        result = self.fn(text)
        expected = 'I the author disapprove'
        self.assertEqual(expected, result)

    def test_chinese_punctuation(self):
        text = '《ESPN》記者（AW）最新報導指出，就在昨日（13號）賽後直言火箭狀況無法修復。'
        result = self.fn(text)
        expected = 'ESPN記者AW最新報導指出就在昨日13號賽後直言火箭狀況無法修復'
        self.assertEqual(expected, result)

    def test_japanese_punctuation(self):
        text = '台湾メディアの聯合新聞網は14日、日本で人気を博しているあるパンのネー' \
               'ミングについて、「香港に失礼だ」との声が上がっていると伝えた。'
        result = self.fn(text)
        expected = '台湾メディアの聯合新聞網は14日日本で人気を博しているあるパンのネー' \
                   'ミングについて香港に失礼だとの声が上がっていると伝えた'
        self.assertEqual(expected, result)

    def test_spanish_punctuation(self):
        text = '!Hola amigo¡'
        result = self.fn(text)
        expected = 'Hola amigo'
        self.assertEqual(expected, result)
