import unittest
from typing import Dict

from text_cleaning.pipelines.generic import \
    FrenchTextCleaningPipeline, \
    FrenchTokensCleaningPipeline


class TestFrenchCleaningPipelines(unittest.TestCase):

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
        self.clean_text = FrenchTextCleaningPipeline(debug=False)
        self.clean_tokens = FrenchTokensCleaningPipeline(debug=False)

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
        'text': 'L’Italie choisit ArcelorMittal pour reprendre la plus grande aciérie d’Europe',
        'expected': ['italie', 'choisit', 'arcelormittal', 'pour', 'reprendre', 
                    'la', 'plus', 'grande', 'aciérie', 'europe']
    },
    {
        'text': 'A 38 jours du premier tour de la présidentielle et en pleine offensive russe en Ukraine',
        'expected': ['numtoken', 'jours', 'du', 'premier', 'tour', 'de', 'la', 'présidentielle', 
                    'et', 'en', 'pleine', 'offensive', 'russe', 'en', 'ukraine']
    },
    {
        'text': 'https://t.co/dpyqd7ePix',
        'expected': []
    },
]
