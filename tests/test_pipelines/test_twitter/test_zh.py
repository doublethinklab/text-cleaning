import unittest
from typing import Dict

from text_cleaning.pipelines.twitter import \
    TwitterMandarinTextCleaningPipeline, \
    TwitterMandarinTokensCleaningPipeline


class TestTwitterMandarinTextCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.rules = {

        }
        self.clean_text = TwitterMandarinTextCleaningPipeline(
            standardization_rules=self.rules, debug=False)

    def _test(self, sample: Dict):
        text = self.clean_text(sample['tweet'])
        self.assertEqual(sample['expected'], text)

    def test_samples(self):
        for sample in text_data:
            self._test(sample)


class TestTwitterMandarinTokensCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.clean_tokens = TwitterMandarinTokensCleaningPipeline()

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
        'tweet': '习近平指出，要坚持互利共赢，构筑伙伴关系。支持联合国发挥统筹协调作用，'
                 '深化全球发展伙伴关系，构建全球发展命运共同体。发达国家要切实履行发展援助'
                 '承诺，为发展中国家提供更多资源。中方提出的全球发展倡议将同联合国2030年'
                 '可持续发展议程深入对接，共同推进全球发展事业。 '
                 'https://t.co/jlXpLynHW0',
        'expected': '习近平指出，要坚持互利共赢，构筑伙伴关系。支持联合国发挥统筹协调作用，'
                 '深化全球发展伙伴关系，构建全球发展命运共同体。发达国家要切实履行发展援助'
                 '承诺，为发展中国家提供更多资源。中方提出的全球发展倡议将同联合国2030年'
                 '可持续发展议程深入对接，共同推进全球发展事业。 '
                 'https://t.co/jlXpLynHW0'
    },
]
tokens_data = [
    {
        'tokens': [
            '习近平', '指出', '，', '要', '坚持', '互利共赢', '，',
            '构筑', '伙伴', '关系', '。', 'https://t.co/jlXpLynHW0',
        ],
        'expected': [
            '习近平', '指出', '要', '坚持', '互利共赢', '构筑', '伙伴', '关系',
        ],
    },
    {
        'tokens': [
            '【', '朝鮮', '成功', '試射', '一', '枚', '高超', '音速', '導彈',
            '】', '據', '朝中社', '6日', '報道', '，', '朝鮮', '5日', '成功',
            '試射', '了', '一', '枚', '高超', '音速', '導彈', '。', '這', '是',
            '朝鮮', '繼', '2021年9月', '成功', '試射', '一', '枚', '“',
            '火星-8', '”', '型', '高超', '音速', '導彈', '後', '，', '第二',
            '次', '試射', '高超', '音速', '導彈', '。',
        ],
        'expected': [
            '朝鮮', '成功', '試射', '一', '枚', '高超', '音速', '導彈',
            '據', '朝中社', '6日', '報道', '朝鮮', '5日', '成功',
            '試射', '了', '一', '枚', '高超', '音速', '導彈', '這', '是',
            '朝鮮', '繼', 'numtoken', '成功', '試射', '一', '枚',
            '火星8', '型', '高超', '音速', '導彈', '後', '第二',
            '次', '試射', '高超', '音速', '導彈',
        ],
    },
]
