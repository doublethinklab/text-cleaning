import unittest

from text_cleaning import replacements as repl
from text_cleaning.functions.text import ReplaceMentions


class TestReplaceMentions(unittest.TestCase):

    def test_case_1(self):
        fn = ReplaceMentions()
        text = '@someone can you hear me?'
        result = fn(text)
        expected = f'{repl.MENTION} can you hear me?'
        self.assertEqual(expected, result)
