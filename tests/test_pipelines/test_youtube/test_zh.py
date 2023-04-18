import unittest

from text_cleaning.pipelines.youtube.zh import CleanChineseYouTubeText, \
    CleanChineseYouTubeTokens


class TestCleanChineseFacebookText(unittest.TestCase):

    def test_case_1(self):
        text = '【“95後”梅派傳人苦練京劇20余年 唱腔醉人】《貴妃醉酒》《霸王別姬》' \
               '《牡丹亭》……他每晚在網絡直播間像朋友一樣與大家分享京劇世界的喜怒哀樂、' \
               '悲歡離合；他是京劇男旦、梅派青衣，師從著名京劇表演藝術家梅蘭芳大師弟' \
               '子張南雲，榮獲第十四屆中國戲曲小梅花十佳金獎；他叫郭雨昂，“95後”小伙' \
               '兒，與時俱進傳承國粹經典。一起來聽醉人唱腔~'
        clean = CleanChineseYouTubeText()
        cleaned = clean(text)
        expected = '【“95後”梅派傳人苦練京劇20余年 唱腔醉人】《貴妃醉酒》《霸王別姬》' \
                   '《牡丹亭》……他每晚在網絡直播間像朋友一樣與大家分享京劇世界的' \
                   '喜怒哀樂、悲歡離合；他是京劇男旦、梅派青衣，師從著名京劇表演藝' \
                   '術家梅蘭芳大師弟子張南雲，榮獲第十四屆中國戲曲小梅花十佳金獎；' \
                   '他叫郭雨昂，“95後”小伙兒，與時俱進傳承國粹經典。一起來聽醉人唱腔~'
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
        clean = CleanChineseYouTubeTokens()
        cleaned = clean(tokens)
        expected = [
            '国家', '统计局', 'numtoken', '发布', '数据', '初步', '核算', '今年',
            '一季度', '中国', '国内', '生产', '总值', 'gdp', 'numtoken', '按不变',
            '价格', '计算', '同比', '增长', 'numtoken', '比', 'numtoken',
            '四季度', '环比', '增长', 'numtoken', '伴随着', '疫情', '防控', '较快',
            '平稳', '转段', '生产', '需求', '企稳回升', '市场', '预期', '明显',
            '改善', '经济', '运行', '开局', '良好']
        self.assertEqual(expected, cleaned)
