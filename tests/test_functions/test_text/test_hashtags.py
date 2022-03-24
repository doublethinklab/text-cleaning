import unittest

from text_cleaning.functions.text import NormalizeWhitespace, RemoveHashtags


class TestRemoveHashtags(unittest.TestCase):

    def test_case_1(self):
        remove = RemoveHashtags()
        text = 'Some tweet #WithHashtag #AndAnother #WeiboStyle# ' \
               '#D1g1tsInHashtag here'
        result = remove(text)
        # normalize resulting spaces
        norm = NormalizeWhitespace()
        result = norm(result)
        expected = 'Some tweet here'
        self.assertEqual(expected, result)
