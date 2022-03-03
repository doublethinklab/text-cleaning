import unittest
from typing import Dict

from text_cleaning.pipelines.generic import \
    JapaneseTextCleaningPipeline, \
    JapaneseTokensCleaningPipeline


class TestJapaneseCleaningPipelines(unittest.TestCase):

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
        self.clean_text = JapaneseTextCleaningPipeline(
            standardization_rules=self.rules, debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(sample['text'])
        self.assertEqual(sample['expected'], text)

    # def test_urls_not_destroyed_by_remove_garbage(self):
    #     text = '大規模なサイバー攻撃は ' \
    #         'https://www.yomiuri.co.jp/world/20220303-OYT1T50284/'
    #     text = self.clean_text(text)
    #     self.assertIn('https://www.yomiuri.co.jp/world/20220303-OYT1T50284/', text)
    
    def test_samples(self):
        for sample in text_data:
            self._test(sample)


class TestJapaneseTokensCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.clean_tokens = JapaneseTokensCleaningPipeline()

    def _test(self, sample: Dict):
        tokens = self.clean_tokens(sample['tokens'])
        if tokens != sample['expected']:
            print('-' * 8)
            print(sample['expected'])
            print(tokens)
        self.assertEqual(sample['expected'], tokens)

    def test_samples(self):
        for sample in tokens_data:
            self._test(sample)




text_data = [
    {
        'text': '秋篠宮さま　この昨年からＣＯＶＩＤ―１９はずっと続いていて',
        'expected': '秋篠宮さま この昨年からcovid19はずっと続いていて'
    }, 
    {
        'text': '世界ボクシング協会（ＷＢＡ）ミドル級スーパー王者の村田諒太',
        'expected': '世界ボクシング協会(wba)ミドル級スーパー王者の村田諒太'
    }
]

tokens_data = [
    {
        'tokens': [
            '歩道', 'を', '走る', '自動', '配達', 'ロボ', '、', 
            'サンフランシスコ', '市', 'が', '走行', '禁止', 'を', '検討',
            'https://t.co/jlXpLynHW0'
        ],
        'expected': [
            '歩道', 'を', '走る', '自動', '配達', 'ロボ', 'サンフランシスコ', 
            '市', 'が', '走行', '禁止', 'を', '検討',
        ],
    },
    {
        'tokens': ['ロンドン', 'は', 'イギリス', 'の', '大', '都市', 'です', '。'],
        'expected': ['ロンドン', 'は', 'イギリス', 'の', '大', '都市', 'です'],
    },
]
