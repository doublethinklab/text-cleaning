import unittest

from text_cleaning import regexps


class TestRegexMatching(unittest.TestCase):

    def test_extraction_from_text(self):
        text = 'Here are some #hashtags including one in #weibostyle#.'
        matches = regexps.extract_hashtags(text=text)
        expected = [
            {
                'text': '#hashtags',
                'start': 14,
                'end': 23,
            },
            {
                'text': '#weibostyle#',
                'start': 41,
                'end': 53,
            },
        ]
        self.assertEqual(expected, matches)

    def test_token_matches(self):
        tokens = ['Not', 'a', '#hashtag', 'and', '#weibostyle#']
        matches = [regexps.matches_target(t, regexps.hashtag) for t in tokens]
        expected = [False, False, True, False, True]
        self.assertEqual(expected, matches)

    def test_urls_case_1(self):
        text = '阅读报道：https://t.co/3kuwsdfQiA https://t.co/wmxtuqGqf8'
        matches = regexps.extract_matches(text, regexps.url)
        expected = [
            {
                'text': 'https://t.co/3kuwsdfQiA',
                'start': 5,
                'end': 28,
            },
            {
                'text': 'https://t.co/wmxtuqGqf8',
                'start': 29,
                'end': 52,
            },
        ]
        self.assertEqual(expected, matches)

    def test_mentions_case_1(self):
        text = '视频作者b站up @director_鹤唳云端 ） '
        matches = regexps.extract_mentions(text)
        expected = [
            {
                'text': '@director_鹤唳云端',
                'start': 9,
                'end': 23,
            },
        ]
        self.assertEqual(expected, matches)
