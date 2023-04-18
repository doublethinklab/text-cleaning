import unittest

from text_cleaning import languages
from text_cleaning.functions.text import \
    NormalizeWhitespace, SingleNewlineToSpace, SingleNewlineToPeriod


class TestNormalizeWhitespace(unittest.TestCase):

    def setUp(self):
        self.fn = NormalizeWhitespace()

    def test_case_1(self):
        text = ' This  is a string\n\nwith non-normal whitespace. '
        result = self.fn(text)
        expected = 'This is a string\nwith non-normal whitespace.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        text = 'Text https://something.com 123  goes◆ here'
        result = self.fn(text)
        expected = 'Text https://something.com 123 goes◆ here'
        self.assertEqual(expected, result)


class TestSingleNewlineToSpace(unittest.TestCase):

    def setUp(self):
        self.fn = SingleNewlineToSpace()

    def test_case_1(self):
        text = """Through COAG and processes such as the Business Advisory
Forum, pursue 
continuous improvements to lift regulatory performance across all areas of 
regulatory practice, with a particular focus on the application of risk-based 
approaches and giving greater attention to reform implementation and 
enforcement. """
        cleaned = self.fn(text)
        expected = 'Through COAG and processes such as the Business ' \
                   'Advisory Forum, pursue  continuous improvements to lift ' \
                   'regulatory performance across all areas of  regulatory ' \
                   'practice, with a particular focus on the application of ' \
                   'risk-based  approaches and giving greater attention to ' \
                   'reform implementation and  enforcement.'
        self.assertEqual(expected, cleaned)


class TestSingleNewlineToPeriod(unittest.TestCase):

    def test_en_case(self):
        text = 'This is my text\nHere it is.'
        clean = SingleNewlineToPeriod(language=languages.en)
        cleaned = clean(text)
        expected = 'This is my text. Here it is.'
        self.assertEqual(expected, cleaned)

    def test_zn_case(self):
        text = '這是我的句子\n在這喔。'
        clean = SingleNewlineToPeriod(language=languages.zh)
        cleaned = clean(text)
        expected = '這是我的句子。在這喔。'
        self.assertEqual(expected, cleaned)
