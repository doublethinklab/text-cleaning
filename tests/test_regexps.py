import re
import unittest

from text_cleaning import regexps


class TestMatchingHashtags(unittest.TestCase):

    def test_extraction_from_text(self):
        text = 'Here are some #hashtags including one in #weibostyle#.'
        matches = regexps.extract_matches(text=text, regexp=regexps.hashtag)
        expected = ['#hashtags', '#weibostyle#']
        self.assertEqual(expected, matches)
