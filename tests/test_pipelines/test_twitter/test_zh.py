import unittest
from typing import Dict

from text_cleaning import replacements
from text_cleaning.pipelines.twitter.zh import *


class TestTwitterMandarinTextCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.rules = {

        }
        self.clean = CleanMandarinTwitterText(debug=False)

    def _test(self, sample: Dict):
        text = self.clean(sample['tweet'])
        self.assertEqual(sample['expected'], text)

    def test_urls_replaced(self):
        text = '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客 ' \
               'https://t.co/KAajTmJG04'
        text = self.clean(text)
        self.assertNotIn('https://t.co/kaajtmjg04', text)
        self.assertIn(replacements.URL, text)

    def test_mentions_kept_intact(self):
        text = '敬请今晚在 @ABCTV 收看《驻外记者》@ForeignOfficial 之《中国的未来》。'
        result = self.clean(text)
        self.assertIn('@abctv', result)
        self.assertIn('@foreignofficial', result)

    def test_samples(self):
        for sample in text_data:
            self._test(sample)


class TestTwitterMandarinTokensCleaningPipeline(unittest.TestCase):

    def setUp(self):
        self.clean = CleanMandarinTwitterTokens()

    def _test(self, sample: Dict):
        tokens = self.clean(sample['tokens'])
        if tokens != sample['expected']:
            print('-' * 8)
            print(sample['expected'])
            print(tokens)
        self.assertEqual(sample['expected'], tokens)

    def test_mentions_kept_intact(self):
        tokens = ['@abctv', '@foreignofficial']
        result = self.clean(tokens)
        self.assertEqual(tokens, result)

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
                 '%s' % replacements.URL
    },
    {
        'tweet': '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客 '
                 'https://t.co/KAajTmJG04',
        'expected': '「大國建造」走進香港迪士尼 迪士尼盼迎來更多大灣區遊客'
                    ' %s' % replacements.URL
    },
]
tokens_data = [
    {
        'tokens': [
            '习近平', '指出', '，', '要', '坚持', '互利共赢', '，',
            '构筑', '伙伴', '关系', '。', replacements.URL,
        ],
        'expected': [
            '习近平', '指出', '要', '坚持', '互利共赢', '构筑', '伙伴', '关系',
            replacements.URL,
        ],
    },
    {
        'tokens': [
            '【', '朝鮮', '成功', '試射', '一', '枚', '高超', '音速', '導彈',
            '】', '據', '朝中社', '6日', '報道', '，', '朝鮮', '5日', '成功',
            '試射', '了', '一', '枚', '高超', '音速', '導彈', '。', '這', '是',
            '朝鮮', '繼', '2021年9月', '成功', '試射', '一', '枚', '“',
            '火星-8', '”', '型', '高超', '音速', '導彈', '後', '，', '第二',
            '次', '試射', '高超', '音速', '#導彈#', '。',
        ],
        'expected': [
            '朝鮮', '成功', '試射', '一', '枚', '高超', '音速', '導彈',
            '據', '朝中社', '6日', '報道', '朝鮮', '5日', '成功',
            '試射', '了', '一', '枚', '高超', '音速', '導彈', '這', '是',
            '朝鮮', '繼', 'numtoken', '成功', '試射', '一', '枚',
            '火星8', '型', '高超', '音速', '導彈', '後', '第二',
            '次', '試射', '高超', '音速', '#導彈',
        ],
    },
]
