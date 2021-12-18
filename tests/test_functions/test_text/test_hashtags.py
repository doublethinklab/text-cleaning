import unittest

from text_cleaning.functions.text import RemoveHashtags


class TestRemoveHashtags(unittest.TestCase):

    def test_case_1(self):
        remove = RemoveHashtags()
        text = 'Some tweet #WithHashtag #AndAnother #D1g1tsInHashtag'
        result = remove(text)
        expected = 'Some tweet'
        self.assertEqual(expected, result)
