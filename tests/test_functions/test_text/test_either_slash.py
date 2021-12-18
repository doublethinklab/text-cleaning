import unittest

from text_cleaning.functions.text import ReplaceEitherSlashWithSpace


class TestReplaceEitherSlashWithSpace(unittest.TestCase):

    def test_case_1(self):
        replace = ReplaceEitherSlashWithSpace()
        text = 'Something/nothing whatever.'
        result = replace(text)
        expected = 'Something nothing whatever.'
        self.assertEqual(expected, result)
