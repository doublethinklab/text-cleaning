import unittest

from text_cleaning import regexps


class TestMatchingHashtags(unittest.TestCase):

    def test_extraction_from_text(self):
        text = 'Here are some #hashtags including one in #weibostyle#.'
        matches = regexps.extract_matches(text=text, regexp=regexps.hashtag)
        expected = ['#hashtags', '#weibostyle#']
        self.assertEqual(expected, matches)

    def test_token_matches(self):
        tokens = ['Not', 'a', '#hashtag', 'and', '#weibostyle#']
        matches = [regexps.matches_target(t, regexps.hashtag) for t in tokens]
        expected = [False, False, True, False, True]
        self.assertEqual(expected, matches)


class TestUrlExtraction(unittest.TestCase):

    def test_case_1(self):
        text = '阅读报道：https://t.co/3kuwsdfQiA https://t.co/wmxtuqGqf8'
        matches = regexps.extract_matches(text, regexps.url)
        expected = ['https://t.co/3kuwsdfQiA', 'https://t.co/wmxtuqGqf8']
        self.assertEqual(expected, matches)
