import unittest

from text_cleaning.pipelines.weibo.zh import *


class TestCleanMandarinWeiboText(unittest.TestCase):

    def setUp(self):
        self.clean = CleanChineseWeiboText()

    def test_html_removed(self):
        text = '五千年史诗！10分钟从上古之战到溥仪退位，中国历史年表超燃影视化混剪！' \
               '<br />' \
               '青山不与兴亡事，只共垂杨伴海潮。' \
               '<br />' \
               '“我们多年轻？上下五千年！”' \
               '<br />' \
               '<a  href="https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E6%96%B0%E4%B8%AD%E5%9B%BD%E6%88%90%E7%AB%8B70%E5%91%A8%E5%B9%B4%23&luicode=10000011&lfid=1076037010131150" data-hide="">' \
               '<span class="surl-text">#新中国成立70周年#</span>' \
               '</a>  ' \
               '<a  href="https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E6%8B%A5%E6%9C%89%E4%BA%94%E5%8D%83%E5%B9%B4%E6%96%87%E6%98%8E%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%E4%BD%93%E9%AA%8C%23&extparam=%23%E6%8B%A5%E6%9C%89%E4%BA%94%E5%8D%83%E5%B9%B4%E6%96%87%E6%98%8E%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%E4%BD%93%E9%AA%8C%23&luicode=10000011&lfid=1076037010131150" data-hide="">' \
               '<span class="surl-text">#拥有五千年文明是怎样的体验#</span>' \
               '</a> ' \
               '（视频作者B站up' \
               '<a href=\'/n/Director_鹤唳云端\'>' \
               '@Director_鹤唳云端' \
               '</a>） ' \
               '<a data-url="http://t.cn/AiE5PEUF" href="https://video.weibo.com/show?fid=1034:4414419816673022" data-hide="">' \
               '<span class=\'url-icon\'>' \
               '<img style=\'width: 1rem;height: 1rem\' src=\'https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_video_default.png\'>' \
               '</span>' \
               '<span class="surl-text">帝吧官微的微博视频</span>' \
               '</a> '
        result = self.clean(text)
        expected = '五千年史诗！10分钟从上古之战到溥仪退位，' \
                   '中国历史年表超燃影视化混剪！ ' \
                   '青山不与兴亡事，只共垂杨伴海潮。 ' \
                   '“我们多年轻？上下五千年！” ' \
                   '#新中国成立70周年# ' \
                   '#拥有五千年文明是怎样的体验# （' \
                   '视频作者b站up @director_鹤唳云端 ） ' \
                   '帝吧官微的微博视频'
        self.assertEqual(expected, result)


class TestCleanMandarinWeiboTokens(unittest.TestCase):

    def setUp(self) -> None:
        self.clean = CleanChineseWeiboTokens()

    def test_hashtags_intact_and_normalized(self):
        tokens = [
            '中国', '历史', '年表', '超燃', '影视化', '混剪', '！',
            '#新中国成立70周年#'
        ]
        result = self.clean(tokens)
        expected = [
            '中国', '历史', '年表', '超燃', '影视化', '混剪', '#新中国成立70周年'
        ]
        self.assertEqual(expected, result)

    def test_mentions_kept_intact(self):
        tokens = ['@director_鹤唳云端 ']
        result = self.clean(tokens)
        self.assertEqual(tokens, result)
