import unittest

from text_cleaning.pipelines.youtube.en \
    import CleanEnglishYouTubeText, CleanEnglishYouTubeTokens


class TestCleanEnglishFacebookText(unittest.TestCase):

    def test_case_1(self):
        text = 'China hopes for substantial steps toward a political ' \
               'solution on the #Yemen conflict, Geng Shuang, China\'s ' \
               'deputy permanent representative to the #UN, said in a UN ' \
               'Security Council meeting on Monday.'
        clean = CleanEnglishYouTubeText()
        cleaned = clean(text)
        expected = 'china hopes for substantial steps toward a political ' \
                   'solution on the #yemen conflict, geng shuang, china ' \
                   'deputy permanent representative to the #un, said in a ' \
                   'un security council meeting on monday.'
        self.assertEqual(expected, cleaned)


class TestCleanEnglishFacebookTokens(unittest.TestCase):

    def test_case_1(self):
        tokens = [
            'china', 'hopes', 'for', 'substantial', 'steps', 'toward', 'a',
            'political', 'solution', 'on', 'the', '#yemen', 'conflict,',
            'geng', 'shuang,', 'china', 'deputy', 'permanent',
            'representative', 'to', 'the', '#un,', 'said', 'in', 'a', 'un',
            'security', 'council', 'meeting', 'on', 'monday.'
        ]
        clean = CleanEnglishYouTubeTokens()
        cleaned = clean(tokens)
        expected = [
            'china', 'hopes', 'for', 'substantial', 'steps', 'toward', 'a',
            'political', 'solution', 'on', 'the', 'yemen', 'conflict', 'geng',
            'shuang', 'china', 'deputy', 'permanent', 'representative', 'to',
            'the', 'un', 'said', 'in', 'a', 'un', 'security', 'council',
            'meeting', 'on', 'monday'
        ]
        self.assertEqual(expected, cleaned)
