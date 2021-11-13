import unittest

from text_cleaning.functions import *


class TestReplaceNumbers(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceNumbers(
            split_replacement=True, only_numbers=False)

    def test_no_split_replacement_leaves_token_intact(self):
        fn = ReplaceNumbers(
            split_replacement=False,
            only_numbers=False)
        tokens = ['10days']
        result = fn(tokens)
        self.assertEqual(['NUMdays'], result)

    def test_split_replacement_splits_token(self):
        fn = ReplaceNumbers(
            split_replacement=True,
            only_numbers=False)
        tokens = ['10days']
        result = fn(tokens)
        self.assertEqual(['NUM', 'days'], result)

    def test_only_numbers_replaces_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=True)
        tokens = ['10']
        result = fn(tokens)
        self.assertEqual(['NUM'], result)

    def test_not_only_numbers_replaces_when_not_only_numbers(self):
        fn = ReplaceNumbers(only_numbers=False)
        text = ['10days']
        result = fn(text)
        self.assertEqual(['NUMdays'], result)

    def test_case_1(self):
        text = 'Iam10yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        text = 'Iam100000000000000yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_3(self):
        text = 'Iam０１yearsexperienced.'
        result = self.fn(text)
        expected = f'Iam{NUM}yearsexperienced.'
        self.assertEqual(expected, result)

    def test_case_4(self):
        tokens = ['123', '123a', 'a123', 'a123b']
        result = self.fn(tokens)
        expected = [NUM, NUM, 'a', 'a', NUM, 'a', NUM, 'b']
        self.assertEqual(expected, result)


class TestReplaceUrls(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceUrls()

    def test_case_1(self):
        tokens = ['Some', 'text', 'https://docs.python.org/3/howto/regex.html']
        result = self.fn(tokens)
        expected = ['Some', 'text', f'{URL}']
        self.assertEqual(expected, result)


class TestRemovePunctuation(unittest.TestCase):

    def setUp(self):
        self.fn = RemovePunctuation()

    def test_english_punctuation(self):
        text = 'I, the "author," disapprove.'
        result = self.fn(text)
        expected = 'I the author disapprove'
        self.assertEqual(expected, result)

    def test_chinese_punctuation(self):
        text = '《ESPN》記者（AW）最新報導指出，就在昨日（13號）賽後直言火箭狀況無法修復。'
        result = self.fn(text)
        expected = 'ESPN記者AW最新報導指出就在昨日13號賽後直言火箭狀況無法修復'
        self.assertEqual(expected, result)

    def test_japanese_punctuation(self):
        text = '台湾メディアの聯合新聞網は14日、日本で人気を博しているあるパンのネー' \
               'ミングについて、「香港に失礼だ」との声が上がっていると伝えた。'
        result = self.fn(text)
        expected = '台湾メディアの聯合新聞網は14日日本で人気を博しているあるパンのネー' \
                   'ミングについて香港に失礼だとの声が上がっていると伝えた'
        self.assertEqual(expected, result)

    def test_spanish_punctuation(self):
        text = '!Hola amigo¡'
        result = self.fn(text)
        expected = 'Hola amigo'
        self.assertEqual(expected, result)


class TestNormalizeWhitespace(unittest.TestCase):

    def setUp(self):
        self.fn = NormalizeWhitespace()

    def test_case_1(self):
        text = ' This  is a string\n\nwith non-normal whitespace. '
        result = self.fn(text)
        expected = 'This is a string\nwith non-normal whitespace.'
        self.assertEqual(expected, result)

    def test_case_2(self):
        text = 'Text https://something.com 123  goes◆ here'
        result = self.fn(text)
        expected = 'Text https://something.com 123 goes◆ here'
        self.assertEqual(expected, result)


class TestReplaceGarbageTokens(unittest.TestCase):

    def setUp(self):
        self.fn = ReplaceGarbage()

    def test_case_1(self):
        text = '◆外交部abc123.?'
        result = self.fn(text)
        expected = f'{JUNK}外交部abc123.?'
        self.assertEqual(expected, result)


class TestRemoveGarbage(unittest.TestCase):

    def setUp(self):
        self.fn = RemoveGarbage(languages=['zh_CN', 'en_US'])

    def test_case_1(self):
        text = '◆外交部abc123.?'
        result = self.fn(text)
        expected = '外交部abc123.?'
        self.assertEqual(expected, result)

    def test_case_2(self):
        text = 'Text https://something.com 123  goes◆ here.'
        result = self.fn(text)
        expected = 'Text https://something.com 123  goes here.'
        self.assertEqual(expected, result)

    def test_chinese_removed_when_not_ordered(self):
        fn = RemoveGarbage(languages=['en_US'])
        text = '◆外交部abc123.?'
        result = fn(text)
        expected = 'abc123.?'
        self.assertEqual(expected, result)

    def test_spanish_case(self):
        fn = RemoveGarbage(languages=['es_ES'])
        text = '◆外交部abc123áéíóúñüÁÉÍÓÚÑÜ'
        result = fn(text)
        expected = 'abc123áéíóúñüÁÉÍÓÚÑÜ'
        self.assertEqual(expected, result)


class TestTraditionalToSimplified(unittest.TestCase):

    def setUp(self):
        self.fn = TraditionalToSimplified()

    def test_case_1(self):
        text = '國家'
        result = self.fn(text)
        expected = '国家'
        self.assertEqual(expected, result)


class TestEntities(unittest.TestCase):

    def setUp(self):
        self.fn = TraditionalToSimplified()

    def test_case_1(self):
        entities = [{'entity': '國家'}]
        result = self.fn(entities)
        expected = [{'entity': '国家'}]
        self.assertEqual(expected, result)


class TestSingleNewlineToSpace(unittest.TestCase):

    def setUp(self):
        self.fn = SingleNewlineToSpace()

    def test_case_1(self):
        text = """Through COAG and processes such as the Business Advisory
Forum, pursue 
continuous improvements to lift regulatory performance across all areas of 
regulatory practice, with a particular focus on the application of risk-based 
approaches and giving greater attention to reform implementation and 
enforcement. """
        cleaned = self.fn(text)
        expected = 'Through COAG and processes such as the Business ' \
                   'Advisory Forum, pursue  continuous improvements to lift ' \
                   'regulatory performance across all areas of  regulatory ' \
                   'practice, with a particular focus on the application of ' \
                   'risk-based  approaches and giving greater attention to ' \
                   'reform implementation and  enforcement.'
        self.assertEqual(expected, cleaned)
