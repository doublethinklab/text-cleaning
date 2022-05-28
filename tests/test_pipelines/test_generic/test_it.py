import unittest
from typing import Dict

from text_cleaning.pipelines.generic import \
    ItalianTextCleaningPipeline, \
    ItalianTokensCleaningPipeline


class TestItalianCleaningPipelines(unittest.TestCase):

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
        self.clean_text = ItalianTextCleaningPipeline(debug=False)
        self.clean_tokens = ItalianTokensCleaningPipeline(debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(
            sample['text'],
            standardization_rules=self.rules)
        tokens = text.split(' ')
        tokens = self.clean_tokens(tokens)
        if tokens != sample['expected']:
            print('-' * 8)
            print(sample['text'])
            print(text)
            print(tokens)
        self.assertEqual(sample['expected'], tokens)

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
        'text': 'Londra è una grande città del Regno Unito #COVID19.',
        'expected': ['londra', 'è', 'una', 'grande', 'città', 'del', 'regno', 'unito', 'covid19']
    },
    {
        'text': 'Il problema è che oltre 30.000 persone over 65 vivono da sole o con meno di 9.000 euro annui.',
        'expected': ['il', 'problema', 'è', 'che', 'oltre', 'numtoken', 'persone', 'over', 'numtoken', 'vivono', 'da', 
                    'sole', 'o', 'con', 'meno', 'di', 'numtoken', 'euro', 'annui']
    },
    {
        'text': 'La #Spagna si impone anche nella seconda sfida di #Coverciano',
        'expected': ['la', 'spagna', 'si', 'impone', 'anche', 'nella', 'seconda', 'sfida', 'di', 'coverciano']
    },
    {
        'text': 'https://t.co/dpyqd7ePix',
        'expected': []
    },
]
