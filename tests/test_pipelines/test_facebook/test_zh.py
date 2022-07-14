import unittest

from text_cleaning.pipelines.facebook.zh import CleanChineseFacebookText, \
    CleanChineseFacebookTokens


class TestCleanChineseFacebookText(unittest.TestCase):

    def test_init_works_without_error(self):
        error = False
        try:
            _ = CleanChineseFacebookText()
        except:
            error = True
        self.assertFalse(error)


class TestCleanChineseFacebookTokens(unittest.TestCase):

    def test_init_works_without_error(self):
        error = False
        try:
            _ = CleanChineseFacebookTokens()
        except:
            error = True
        self.assertFalse(error)
