import unittest

from text_cleaning.pipelines import *


class TestStandardTextCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = StandardTextCleaningPipeline(languages=['en_US'])

    def test_case_1(self):
        text = 'Text 123  goes◆ here.'
        result = self.pipeline(text)
        expected = 'Text 123 goes here.'
        self.assertEqual(expected, result)


class TestStandardTokensCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = StandardTokensCleaningPipeline()

    def test_case_1(self):
        tokens = [
            'Text',
            'https://something.com',
            '123',
            'goes?',
            'here',
            '.',
        ]
        result = self.pipeline(tokens)
        expected = ['Text', f'{URL}', f'{NUM}', 'goes', 'here']
        self.assertEqual(expected, result)


class TestStandardZhTokensCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.clean = StandardZhTokensCleaningPipeline()

    def test_case_1(self):
        tokens = [
            'Text',
            'https://something.com',
            '123',
            'goes?',
            'here',
            '國家',
            '.',
        ]
        result = self.clean(tokens)
        expected = ['Text', f'{URL}', f'{NUM}', 'goes', 'here', '国家']
        self.assertEqual(expected, result)
