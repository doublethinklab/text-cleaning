import unittest
from typing import Dict

from text_cleaning.pipelines.generic import \
    SpanishTextCleaningPipeline, \
    SpanishTokensCleaningPipeline


class TestSpanishCleaningPipelines(unittest.TestCase):

    def setUp(self):
        self.rules = {
            'usa': ['U.S.A.', 'USA', 'U.S.', 'US'],
            'covid19': ['COVID-19', 'COVID19', 'COVID',
                        'Covid-19', 'Covid',
                        'covid-19', 'covid',
                        '#COVID-19', '#COVID19', '#COVID',
                        '#covid-19', '#covid', '#Covid-19', 'Covid'],
            'worldhealthorganization': ['WHO', 'W.H.O.',
                                        'World Health Organization'],
        }
        self.clean_text = SpanishTextCleaningPipeline(
            standardization_rules=self.rules, debug=False)
        self.clean_tokens = SpanishTokensCleaningPipeline(debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(sample['text'])
        tokens1 = text.split(' ')
        tokens2 = self.clean_tokens(tokens1)
        if tokens2 != sample['expected']:
            print('-' * 8)
            print(sample['text'])
            print(text)
            print(tokens1)
        self.assertEqual(sample['expected'], tokens2)

    def test_urls_not_destroyed_by_remove_garbage(self):
        text = 'Azar says https://t.co/CwnG8H94mh https://t.co/E1ROgNAqlw'
        text = self.clean_text(text)
        self.assertIn('https://t.co/cwng8h94mh', text)
        self.assertIn('https://t.co/e1rognaqlw', text)

    def test_samples(self):
        for sample in data:
            self._test(sample)


data = [
    {
        'text': '#¿Dónde está encuentra la capital de Argentina?',
        'expected': ['dónde', 'está', 'encuentra', 'la', 'capital', 'de', 'argentina']
    },
    {
        'text': 'El covid de China impide que todos viajen al extranjero',
        'expected': ['el', 'covid19', 'de', 'china', 'impide', 'que', 'todos', 'viajen', 'al', 'extranjero']
    },
    {
        'text': '＃环球时报Yo, señor, no soy malo, aunque no me faltarían motivos para serlo.\u3000',
        'expected': ['yo', 'señor', 'no', 'soy', 'malo', 'aunque', 'no', 'me', 'faltarían', 'motivos', 'para', 'serlo']
    },
    {
        'text': 'https://t.co/dpyqd7ePix',
        'expected': []
    },
]
