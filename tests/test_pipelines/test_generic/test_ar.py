import unittest
from typing import Dict

from text_cleaning.pipelines.generic import \
    ArabicTextCleaningPipeline, \
    ArabicTokensCleaningPipeline


class TestArabicTextCleaningPipelines(unittest.TestCase):

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
        self.clean_text = ArabicTextCleaningPipeline(
            standardization_rules=self.rules, debug=False)
        # self.clean_tokens = ArabicTokensCleaningPipeline(debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(sample['text'])
        self.assertEqual(sample['expected'], text)

    def test_samples(self):
        for sample in data:
            self._test(sample)


data = [
    {
        'text': '#COVID19 يقود شي جين بينغ الصين على طريق التنمية الصحيح',
        'expected': 'covid19 يقود شي جين بينغ الصين على طريق التنمية الصحيح',
    },
    {
        'text': ' 环球时报يتم حصاد قطن شينجيانغ بالآلة',
        'expected': 'يتم حصاد قطن شينجيانغ بالآلة'
    },
]
