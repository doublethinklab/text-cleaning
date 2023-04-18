import unittest

from text_cleaning.pipelines.generic.zh \
    import CleanGenericChineseText, CleanGenericChineseTokens


class TestCleanChineseFacebookText(unittest.TestCase):

    def test_case_1(self):
        text = """国家统计局4月18日发布数据
初步核算
今年一季度中国国内生产总值（GDP）284997亿元
按不变价格计算，同比增长4.5%
比2022年四季度环比增长2.2%
伴随着疫情防控较快平稳转段
生产需求企稳回升，市场预期明显改善
经济运行开局良好"""
        clean = CleanGenericChineseText()
        cleaned = clean(text)
        expected = """国家统计局4月18日发布数据
初步核算
今年一季度中国国内生产总值(gdp)284997亿元
按不变价格计算,同比增长4.5%
比2022年四季度环比增长2.2%
伴随着疫情防控较快平稳转段
生产需求企稳回升,市场预期明显改善
经济运行开局良好"""
        self.assertEqual(expected, cleaned)


class TestCleanChineseFacebookTokens(unittest.TestCase):

    def test_case_1(self):
        tokens = [
            '国家', '统计局', '4月18日', '发布', '数据',
            '初步', '核算',
            '今年', '一季度', '中国', '国内', '生产', '总值', '（gdp）', '284997亿元',
            '按不变', '价格', '计算', '，', '同比', '增长', '4.5%',
            '比', '2022年', '四季度', '环比', '增长', '2.2%',
            '伴随着', '疫情', '防控', '较快', '平稳', '转段',
            '生产', '需求', '企稳回升', '，', '市场', '预期', '明显', '改善',
            '经济', '运行', '开局', '良好',
        ]
        clean = CleanGenericChineseTokens()
        cleaned = clean(tokens)
        expected = [
            '国家', '统计局', 'numtoken', '发布', '数据', '初步', '核算', '今年',
            '一季度', '中国', '国内', '生产', '总值', 'gdp', 'numtoken', '按不变',
            '价格', '计算', '同比', '增长', 'numtoken', '比', 'numtoken',
            '四季度', '环比', '增长', 'numtoken', '伴随着', '疫情', '防控', '较快',
            '平稳', '转段', '生产', '需求', '企稳回升', '市场', '预期', '明显',
            '改善', '经济', '运行', '开局', '良好']
        self.assertEqual(expected, cleaned)
